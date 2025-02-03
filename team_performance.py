from get_football_data import get_league_id, get_team_id, get_team_stats


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


if __name__ == "__main__":
    league_id = get_league_id()
    team_name = "Bournemouth"
    team_id = get_team_id(team_name=team_name)
    stats = get_team_stats(league_id=league_id, team_id=team_id)

    win_percentage = get_win_percentage(stats=stats)
    avg_goals_scored = get_average_goals_scored(stats=stats)
    avg_goals_conceded = get_average_goals_conceded(stats=stats)
    print(
        f"Team stats for {team_name} are: \n"
        f"Win percentage is: {win_percentage} \n"
        f"Avg goals scored are: {avg_goals_scored} \n"
        f"Average conceded goals are: {avg_goals_conceded} \n"
    )
