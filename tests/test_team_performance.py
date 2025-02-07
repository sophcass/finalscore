import pytest

from team_performance import (
    get_average_goals_conceded,
    get_average_goals_scored,
    get_num_fixtures_played,
    get_recent_form_index,
    get_win_percentage,
)


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
