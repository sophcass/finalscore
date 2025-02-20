from unittest import mock

import pytest

from get_football_data import get_team_standings
from team_performance import (
    get_average_goals_conceded,
    get_average_goals_scored,
    get_num_fixtures_played,
    get_rankings_in_league,
    get_recent_form_index,
    get_win_percentage,
)


@mock.patch("get_football_data.get_data_from_rapidapi")
def test_get_team_standings(mock_get_data_from_rapidapi, standings_by_league_id_data):
    # Arrange
    mock_get_data_from_rapidapi.return_value = standings_by_league_id_data
    league_id = 39
    team_standings = get_team_standings(league_id=league_id)

    expected_rankings_in_league = {
        40: 1,
        42: 2,
        65: 3,
        50: 4,
        35: 5,
        49: 6,
        34: 7,
        36: 8,
        66: 9,
        51: 10,
        55: 11,
        47: 12,
        52: 13,
        45: 14,
        33: 15,
        48: 16,
        39: 17,
        57: 18,
        46: 19,
        41: 20,
    }

    # Act
    rankings_in_league = get_rankings_in_league(standings=team_standings)

    # Assert
    assert rankings_in_league == expected_rankings_in_league


def test_get_num_fixtures_played(team_stats):
    # Act
    num_fixtures_played = get_num_fixtures_played(stats=team_stats)

    # Assert
    assert num_fixtures_played == 23


def test_get_win_percentage(team_stats):
    # Act
    win_percentage = get_win_percentage(stats=team_stats)

    # Assert
    assert win_percentage == 26.08695652173913


def test_get_average_goals_scored(team_stats):
    # Act
    avg_goals_scored = get_average_goals_scored(stats=team_stats)

    # Assert
    assert avg_goals_scored == 1.0


def test_get_average_goals_conceded(team_stats):
    # Act
    avg_goals_conceded = get_average_goals_conceded(stats=team_stats)

    # Assert
    assert avg_goals_conceded == 1.2173913043478262


@pytest.mark.parametrize(
    "num_fixtures_available, expected_recent_form_index",
    [
        (5, 1.8),
        (4, 2.2),
        (3, 1.6666666666666667),
    ],
)
def test_get_recent_form_index(
    num_fixtures_available, expected_recent_form_index, match_stats
):
    # Arrange
    team_id = 45
    match_stats = match_stats[:num_fixtures_available]

    # Act
    recent_form_index = get_recent_form_index(match_stats=match_stats, team_id=team_id)

    # Assert
    assert recent_form_index == expected_recent_form_index
