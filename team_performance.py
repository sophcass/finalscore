import argparse
from datetime import datetime

from get_football_data import (
    get_league_id,
    get_match_stats,
    get_team_highest_ranked_league_id,
    get_team_highest_ranked_league_name,
    get_team_id,
    get_team_stats,
)

NUM_FIXTURES_THRESHOLD = 5


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


def get_recent_form_index(match_stats: list[dict], team_id: int) -> float:
    today = datetime.now().date()
    match_results = []
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

        if home_goals_scored == away_goals_scored:
            match_results.append(1)  # Draw
        elif home_goals_scored > away_goals_scored:
            match_results.append(3 if home_team_id == team_id else 0)
        else:
            match_results.append(3 if away_team_id == team_id else 0)

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get performance metrics for a football team in a given league"
    )
    parser.add_argument(
        "--league", required=True, help="the league name. E.g. Premier League"
    )
    parser.add_argument("--team", required=True, help="the team name. E.g. Everton")
    args = parser.parse_args()

    league_name = args.league
    team_name = args.team

    league_id = get_league_id(league_name=league_name)
    team_id = get_team_id(team_name=team_name)

    team_stats = get_team_stats(league_id=league_id, team_id=team_id)

    num_fixtures_played = get_num_fixtures_played(stats=team_stats)
    print(
        f"{num_fixtures_played} fixtures played in the {league_name} by {team_name}\n"
    )
    if num_fixtures_played < NUM_FIXTURES_THRESHOLD:
        team_primary_league_id = get_team_highest_ranked_league_id(team_id=team_id)
        team_primary_league_name = get_team_highest_ranked_league_name(team_id=team_id)
        print(
            f"Looking at stats from {team_primary_league_name} as less than {NUM_FIXTURES_THRESHOLD} fixtures played in the {league_name}\n"
        )

        team_stats = get_team_stats(league_id=team_primary_league_id, team_id=team_id)

        num_fixtures_played = get_num_fixtures_played(stats=team_stats)
        print(
            f"{num_fixtures_played} fixtures played in the {team_primary_league_name} by {team_name}\n"
        )

        match_stats = get_match_stats(league_id=team_primary_league_id, team_id=team_id)
    else:
        match_stats = get_match_stats(league_id=league_id, team_id=team_id)

    win_percentage = get_win_percentage(stats=team_stats)
    avg_goals_scored = get_average_goals_scored(stats=team_stats)
    avg_goals_conceded = get_average_goals_conceded(stats=team_stats)
    print(
        f"Win percentage is: {win_percentage} \n"
        f"Avg goals scored are: {avg_goals_scored} \n"
        f"Average conceded goals are: {avg_goals_conceded} \n"
    )

    recent_form_index = get_recent_form_index(match_stats=match_stats, team_id=team_id)
    print(f"Recent form index is {recent_form_index}")
