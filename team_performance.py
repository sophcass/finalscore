import argparse
from datetime import datetime

from get_football_data import (
    get_league_id,
    get_match_stats,
    get_team_highest_ranked_league_id,
    get_team_highest_ranked_league_name,
    get_team_id,
    get_team_standings,
    get_team_stats,
)

NUM_FIXTURES_THRESHOLD = 5


def get_rankings_in_league(standings: list[dict]) -> dict:
    rankings_in_league = dict()
    for standing in standings:
        team_id = standing["team"]["id"]
        rankings_in_league[team_id] = standing["rank"]

    return rankings_in_league


def get_num_fixtures_played(stats: dict) -> int:
    return stats["fixtures"]["played"]["total"]


def get_win_percentage(stats: dict) -> int:
    total_matches_played = stats["fixtures"]["played"]["total"]
    total_wins = stats["fixtures"]["wins"]["total"]

    win_percentage = (total_wins / total_matches_played) * 100
    return win_percentage


def get_average_goals_scored(stats: dict) -> int:
    total_matches_played = stats["fixtures"]["played"]["total"]
    total_goals_scored = stats["goals"]["for"]["total"]["total"]

    avg_goals_scored = total_goals_scored / total_matches_played
    return avg_goals_scored


def get_average_goals_conceded(stats: dict) -> int:
    total_matches_played = stats["fixtures"]["played"]["total"]
    total_goals_conceded = stats["goals"]["against"]["total"]["total"]

    avg_goals_conceded = total_goals_conceded / total_matches_played
    return avg_goals_conceded


def get_recent_form_index(
    match_stats: list[dict],
    team_id: int,
    rankings_in_league: dict,
) -> float:
    today = datetime.now().date()
    match_results = []
    num_teams_in_league = len(rankings_in_league)
    weights = [5, 4, 3, 2, 1]

    for fixture in match_stats[::-1]:
        fixture_timestamp = fixture["fixture"]["timestamp"]
        fixture_timestamp = datetime.fromtimestamp(fixture_timestamp)

        if fixture_timestamp.date() >= today:
            continue  # Skip future matches

        home_team_id = fixture["teams"]["home"]["id"]
        away_team_id = fixture["teams"]["away"]["id"]

        home_goals_scored = fixture["goals"]["home"]
        away_goals_scored = fixture["goals"]["away"]

        if home_goals_scored is None or away_goals_scored is None:
            continue  # Match was postponed

        opponent_id = away_team_id if home_team_id == team_id else home_team_id
        opponent_rank = rankings_in_league.get(
            opponent_id, num_teams_in_league
        )  # Default to last place if unknown

        if home_goals_scored == away_goals_scored:
            match_result = 1  # Draw
        elif home_goals_scored > away_goals_scored:
            match_result = 3 if home_team_id == team_id else 0
        else:
            match_result = 3 if away_team_id == team_id else 0

        difficulty_multiplier = 1 + (num_teams_in_league - opponent_rank) / (
            2 * num_teams_in_league
        )
        adjusted_result = match_result * difficulty_multiplier

        match_results.append(adjusted_result)

        if len(match_results) >= 5:
            break

    if not match_results:
        raise Exception("No match data")

    weights = weights[(len(weights) - len(match_results)) :]
    weighted_sum = sum(
        recent_goal * weight for recent_goal, weight in zip(match_results, weights)
    )
    recent_form_index = weighted_sum / sum(weights)

    return recent_form_index


def get_valid_team_stats(league_id: int, team_id: int) -> dict:
    team_stats = get_team_stats(league_id=league_id, team_id=team_id)
    num_fixtures_played = get_num_fixtures_played(team_stats)

    if num_fixtures_played < NUM_FIXTURES_THRESHOLD:
        fallback_league_id = get_team_highest_ranked_league_id(team_id)
        fallback_league_name = get_team_highest_ranked_league_name(team_id)

        print(
            f"Not enough fixtures in the given league. Using stats from {fallback_league_name} instead."
        )

        return get_team_stats(league_id=fallback_league_id, team_id=team_id)

    return team_stats


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get performance metrics for a football team in a given league"
    )
    parser.add_argument(
        "--league", required=True, help="the league name. E.g. Premier League"
    )
    parser.add_argument("--team", required=True, help="the team name. E.g. Everton")
    parser.add_argument(
        "--country", required=False, help="the country the team is from. E.g. England"
    )
    args = parser.parse_args()

    league_name = args.league
    team_name = args.team
    country = args.country

    league_id = get_league_id(league_name=league_name, country=country)
    team_id = get_team_id(team_name=team_name, country=country)

    standings = get_team_standings(league_id=league_id)
    rankings_in_league = get_rankings_in_league(standings=standings)

    team_rank_in_league = rankings_in_league.get(team_id)
    print(f"{team_name} is {team_rank_in_league} in the {league_name}")

    team_stats = get_valid_team_stats(league_id=league_id, team_id=team_id)
    match_stats = get_match_stats(league_id=league_id, team_id=team_id)

    num_fixtures_played = get_num_fixtures_played(stats=team_stats)
    print(
        f"{num_fixtures_played} fixtures played in the {league_name} by {team_name}\n"
    )

    win_percentage = get_win_percentage(stats=team_stats)
    avg_goals_scored = get_average_goals_scored(stats=team_stats)
    avg_goals_conceded = get_average_goals_conceded(stats=team_stats)
    recent_form_index = get_recent_form_index(
        match_stats=match_stats, team_id=team_id, rankings_in_league=rankings_in_league
    )

    print(
        f"Win percentage is: {win_percentage} \n"
        f"Avg goals scored are: {avg_goals_scored} \n"
        f"Average conceded goals are: {avg_goals_conceded} \n"
        f"Recent form index is {recent_form_index}"
    )
