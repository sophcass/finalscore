import http.client
import json
import os
from typing import Any
from urllib.parse import urlencode

from diskcache import Cache

cache = Cache("local")

ENGLISH_FOOTBALL_LEAGUES = {
    "Premier League": 1,
    "Championship": 2,
    "League One": 3,
    "League Two": 4,
    "National League": 5,
}


def get_data_from_rapidapi(path: str) -> dict:
    api_host = "api-football-v1.p.rapidapi.com"
    key = os.getenv("RAPIDAPI_KEY")

    if not key:
        raise ValueError("RAPIDAPI_KEY environment variable is not set.")

    headers = {
        "x-rapidapi-key": key,
        "x-rapidapi-host": api_host,
    }

    try:
        conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")
        conn.request("GET", path, headers=headers)
        response = conn.getresponse()
        if response.status != 200:
            raise ValueError(
                f"API request failed with status {response.status}: {response.reason}"
            )
        return json.loads(response.read().decode("utf-8"))
    except (http.client.HTTPException, json.JSONDecodeError) as e:
        raise ValueError(f"Error fetching data from API: {e}")


@cache.memoize()
def get_league_id(league_name: str) -> int:
    base_url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

    query_params = {"name": league_name, "code": "GB-ENG"}
    path = f"{base_url}?{urlencode(query_params)}"
    data = get_data_from_rapidapi(path=path)

    leagues = data.get("response", [])

    if not leagues:
        raise ValueError("No leagues found in the response.")

    if len(leagues) > 1:
        raise ValueError("More than one league in response")

    league = leagues[0]
    league_id = league["league"]["id"]  # 39 - to be used in other API calls

    return league_id


@cache.memoize()
def get_team_id(team_name: str) -> int:
    base_url = "https://api-football-v1.p.rapidapi.com/v3/teams"

    query_params = {"name": team_name}
    path = f"{base_url}?{urlencode(query_params)}"
    data = get_data_from_rapidapi(path=path)

    teams = data.get("response", [])

    if not teams:
        raise ValueError("No teams found in the response.")

    if len(teams) > 1:
        raise ValueError("More than one team in response")

    team = teams[0]
    team_id = team["team"]["id"]  # 45 - to be used in other API calls

    return team_id


@cache.memoize()
def get_team_stats(league_id: int, team_id: int) -> dict:
    base_url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

    query_params = {"league": league_id, "season": "2024", "team": team_id}
    path = f"{base_url}?{urlencode(query_params)}"
    data = get_data_from_rapidapi(path=path)

    stats = data.get("response", [])

    return stats


@cache.memoize()
def get_match_stats(league_id: int, team_id: int) -> list[dict]:
    base_url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

    query_params = {"league": league_id, "season": "2024", "team": team_id}
    path = f"{base_url}?{urlencode(query_params)}"
    data = get_data_from_rapidapi(path=path)

    stats = data.get("response", [])

    return stats
