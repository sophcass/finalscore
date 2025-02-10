from unittest import mock

import pytest

from get_football_data import (
    get_highest_ranked_league,
    get_team_highest_ranked_league_id,
    get_team_highest_ranked_league_name,
)


@mock.patch("get_football_data.get_data_from_rapidapi")
def test_get_highest_ranked_league(mock_get_data_from_rapidapi, leagues_data):
    # Arrange
    mock_get_data_from_rapidapi.return_value = leagues_data
    team_id = 44

    expected_highest_ranked_league_name = "Championship"

    # Act
    highest_ranked_league = get_highest_ranked_league(team_id=team_id)

    # Assert
    assert (
        highest_ranked_league["league"]["name"] == expected_highest_ranked_league_name
    )


@mock.patch("get_football_data.get_data_from_rapidapi")
def test_get_team_highest_ranked_league_name(mock_get_data_from_rapidapi, leagues_data):
    # Arrange
    mock_get_data_from_rapidapi.return_value = leagues_data
    team_id = 44

    expected_highest_ranked_league_name = "Championship"

    # Act
    highest_ranked_league_name = get_team_highest_ranked_league_name(team_id=team_id)

    # Assert
    assert highest_ranked_league_name == expected_highest_ranked_league_name


@mock.patch("get_football_data.get_data_from_rapidapi")
def test_get_team_highest_ranked_league_id(mock_get_data_from_rapidapi, leagues_data):
    # Arrange
    mock_get_data_from_rapidapi.return_value = leagues_data
    team_id = 44

    expected_highest_ranked_league_id = 40

    # Act
    highest_ranked_league_id = get_team_highest_ranked_league_id(team_id=team_id)

    # Assert
    assert highest_ranked_league_id == expected_highest_ranked_league_id
