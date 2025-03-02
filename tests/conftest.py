import pytest


@pytest.fixture
def team_stats():
    return {
        "league": {
            "id": 39,
            "name": "Premier League",
            "country": "England",
            "logo": "https://media.api-sports.io/football/leagues/39.png",
            "flag": "https://media.api-sports.io/flags/gb-eng.svg",
            "season": 2024,
        },
        "team": {
            "id": 45,
            "name": "Everton",
            "logo": "https://media.api-sports.io/football/teams/45.png",
        },
        "form": "LLLLDWDWDLDDLWDDDLLLWWW",
        "fixtures": {
            "played": {"home": 12, "away": 11, "total": 23},
            "wins": {"home": 4, "away": 2, "total": 6},
            "draws": {"home": 4, "away": 4, "total": 8},
            "loses": {"home": 4, "away": 5, "total": 9},
        },
        "goals": {
            "for": {
                "total": {"home": 16, "away": 7, "total": 23},
                "average": {"home": "1.3", "away": "0.6", "total": "1.0"},
                "minute": {
                    "0-15": {"total": 5, "percentage": "25.00%"},
                    "16-30": {"total": 4, "percentage": "20.00%"},
                    "31-45": {"total": 4, "percentage": "20.00%"},
                    "46-60": {"total": 5, "percentage": "25.00%"},
                    "61-75": {"total": None, "percentage": None},
                    "76-90": {"total": 1, "percentage": "5.00%"},
                    "91-105": {"total": 1, "percentage": "5.00%"},
                    "106-120": {"total": None, "percentage": None},
                },
                "under_over": {
                    "0.5": {"over": 11, "under": 12},
                    "1.5": {"over": 7, "under": 16},
                    "2.5": {"over": 3, "under": 20},
                    "3.5": {"over": 2, "under": 21},
                    "4.5": {"over": 0, "under": 23},
                },
            },
            "against": {
                "total": {"home": 13, "away": 15, "total": 28},
                "average": {"home": "1.1", "away": "1.4", "total": "1.2"},
                "minute": {
                    "0-15": {"total": 4, "percentage": "12.90%"},
                    "16-30": {"total": 2, "percentage": "6.45%"},
                    "31-45": {"total": 3, "percentage": "9.68%"},
                    "46-60": {"total": 6, "percentage": "19.35%"},
                    "61-75": {"total": 6, "percentage": "19.35%"},
                    "76-90": {"total": 7, "percentage": "22.58%"},
                    "91-105": {"total": 3, "percentage": "9.68%"},
                    "106-120": {"total": None, "percentage": None},
                },
                "under_over": {
                    "0.5": {"over": 14, "under": 9},
                    "1.5": {"over": 7, "under": 16},
                    "2.5": {"over": 5, "under": 18},
                    "3.5": {"over": 2, "under": 21},
                    "4.5": {"over": 0, "under": 23},
                },
            },
        },
        "biggest": {
            "streak": {"wins": 1, "draws": 3, "loses": 4},
            "wins": {"home": "4-0", "away": "0-2"},
            "loses": {"home": "0-3", "away": "4-0"},
            "goals": {"for": {"home": 4, "away": 2}, "against": {"home": 3, "away": 4}},
        },
        "clean_sheet": {"home": 5, "away": 4, "total": 9},
        "failed_to_score": {"home": 6, "away": 6, "total": 12},
        "penalty": {
            "scored": {"total": 1, "percentage": "100.00%"},
            "missed": {"total": 0, "percentage": "0%"},
            "total": 1,
        },
        "lineups": [
            {"formation": "4-2-3-1", "played": 19},
            {"formation": "4-3-3", "played": 4},
        ],
        "cards": {
            "yellow": {
                "0-15": {"total": 3, "percentage": "6.25%"},
                "16-30": {"total": 4, "percentage": "8.33%"},
                "31-45": {"total": 7, "percentage": "14.58%"},
                "46-60": {"total": 10, "percentage": "20.83%"},
                "61-75": {"total": 5, "percentage": "10.42%"},
                "76-90": {"total": 15, "percentage": "31.25%"},
                "91-105": {"total": 4, "percentage": "8.33%"},
                "106-120": {"total": None, "percentage": None},
            },
            "red": {
                "0-15": {"total": None, "percentage": None},
                "16-30": {"total": None, "percentage": None},
                "31-45": {"total": None, "percentage": None},
                "46-60": {"total": None, "percentage": None},
                "61-75": {"total": 1, "percentage": "100.00%"},
                "76-90": {"total": None, "percentage": None},
                "91-105": {"total": None, "percentage": None},
                "106-120": {"total": None, "percentage": None},
            },
        },
    }


@pytest.fixture
def match_stats():
    return [
        {
            "fixture": {
                "id": 1208065,
                "referee": "Darren England, England",
                "timezone": "UTC",
                "date": "2024-09-21T14:00:00+00:00",
                "timestamp": 1726927200,
                "periods": {"first": 1726927200, "second": 1726930800},
                "venue": {
                    "id": 547,
                    "name": "King Power Stadium",
                    "city": "Leicester, Leicestershire",
                },
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": None,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 5",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 46,
                    "name": "Leicester",
                    "logo": "https://media.api-sports.io/football/teams/46.png",
                    "winner": None,
                },
                "away": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": None,
                },
            },
            "goals": {"home": 1, "away": 1},
            "score": {
                "halftime": {"home": 0, "away": 1},
                "fulltime": {"home": 1, "away": 1},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208075,
                "referee": "Andy Madley, England",
                "timezone": "UTC",
                "date": "2024-09-28T14:00:00+00:00",
                "timestamp": 1727532000,
                "periods": {"first": 1727532000, "second": 1727535600},
                "venue": {"id": 8560, "name": "Goodison Park", "city": "Liverpool"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 5,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 6",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": True,
                },
                "away": {
                    "id": 52,
                    "name": "Crystal Palace",
                    "logo": "https://media.api-sports.io/football/teams/52.png",
                    "winner": False,
                },
            },
            "goals": {"home": 2, "away": 1},
            "score": {
                "halftime": {"home": 0, "away": 1},
                "fulltime": {"home": 2, "away": 1},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208087,
                "referee": "Craig Pawson, England",
                "timezone": "UTC",
                "date": "2024-10-05T16:30:00+00:00",
                "timestamp": 1728145800,
                "periods": {"first": 1728145800, "second": 1728149400},
                "venue": {"id": 8560, "name": "Goodison Park", "city": "Liverpool"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 5,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 7",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": None,
                },
                "away": {
                    "id": 34,
                    "name": "Newcastle",
                    "logo": "https://media.api-sports.io/football/teams/34.png",
                    "winner": None,
                },
            },
            "goals": {"home": 0, "away": 0},
            "score": {
                "halftime": {"home": 0, "away": 0},
                "fulltime": {"home": 0, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208093,
                "referee": "Michael Oliver, England",
                "timezone": "UTC",
                "date": "2024-10-19T14:00:00+00:00",
                "timestamp": 1729346400,
                "periods": {"first": 1729346400, "second": 1729350000},
                "venue": {
                    "id": 545,
                    "name": "Portman Road",
                    "city": "Ipswich, Suffolk",
                },
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": None,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 8",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 57,
                    "name": "Ipswich",
                    "logo": "https://media.api-sports.io/football/teams/57.png",
                    "winner": False,
                },
                "away": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": True,
                },
            },
            "goals": {"home": 0, "away": 2},
            "score": {
                "halftime": {"home": 0, "away": 2},
                "fulltime": {"home": 0, "away": 2},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208109,
                "referee": "John Brooks, England",
                "timezone": "UTC",
                "date": "2024-10-26T16:30:00+00:00",
                "timestamp": 1729960200,
                "periods": {"first": 1729960200, "second": 1729963800},
                "venue": {"id": 8560, "name": "Goodison Park", "city": "Liverpool"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 7,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 9",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": None,
                },
                "away": {
                    "id": 36,
                    "name": "Fulham",
                    "logo": "https://media.api-sports.io/football/teams/36.png",
                    "winner": None,
                },
            },
            "goals": {"home": 1, "away": 1},
            "score": {
                "halftime": {"home": 0, "away": 0},
                "fulltime": {"home": 1, "away": 1},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208120,
                "referee": "Andy Madley, England",
                "timezone": "UTC",
                "date": "2024-11-02T15:00:00+00:00",
                "timestamp": 1730559600,
                "periods": {"first": 1730559600, "second": 1730563200},
                "venue": {
                    "id": 585,
                    "name": "St. Mary's Stadium",
                    "city": "Southampton, Hampshire",
                },
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 8,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 10",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 41,
                    "name": "Southampton",
                    "logo": "https://media.api-sports.io/football/teams/41.png",
                    "winner": True,
                },
                "away": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": False,
                },
            },
            "goals": {"home": 1, "away": 0},
            "score": {
                "halftime": {"home": 0, "away": 0},
                "fulltime": {"home": 1, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208131,
                "referee": "Stuart Attwell, England",
                "timezone": "UTC",
                "date": "2024-11-09T15:00:00+00:00",
                "timestamp": 1731164400,
                "periods": {"first": 1731164400, "second": 1731168000},
                "venue": {"id": 598, "name": "London Stadium", "city": "London"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 5,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 11",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 48,
                    "name": "West Ham",
                    "logo": "https://media.api-sports.io/football/teams/48.png",
                    "winner": None,
                },
                "away": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": None,
                },
            },
            "goals": {"home": 0, "away": 0},
            "score": {
                "halftime": {"home": 0, "away": 0},
                "fulltime": {"home": 0, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208136,
                "referee": "Chris Kavanagh, England",
                "timezone": "UTC",
                "date": "2024-11-23T15:00:00+00:00",
                "timestamp": 1732374000,
                "periods": {"first": 1732374000, "second": 1732377600},
                "venue": {"id": 8560, "name": "Goodison Park", "city": "Liverpool"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 4,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 12",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": None,
                },
                "away": {
                    "id": 55,
                    "name": "Brentford",
                    "logo": "https://media.api-sports.io/football/teams/55.png",
                    "winner": None,
                },
            },
            "goals": {"home": 0, "away": 0},
            "score": {
                "halftime": {"home": 0, "away": 0},
                "fulltime": {"home": 0, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208148,
                "referee": "John Brooks, England",
                "timezone": "UTC",
                "date": "2024-12-01T13:30:00+00:00",
                "timestamp": 1733059800,
                "periods": {"first": 1733059800, "second": 1733063400},
                "venue": {"id": 556, "name": "Old Trafford", "city": "Manchester"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 4,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 13",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 33,
                    "name": "Manchester United",
                    "logo": "https://media.api-sports.io/football/teams/33.png",
                    "winner": True,
                },
                "away": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": False,
                },
            },
            "goals": {"home": 4, "away": 0},
            "score": {
                "halftime": {"home": 2, "away": 0},
                "fulltime": {"home": 4, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208156,
                "referee": "Salisbury Michael, England",
                "timezone": "UTC",
                "date": "2024-12-04T19:30:00+00:00",
                "timestamp": 1733340600,
                "periods": {"first": 1733340600, "second": 1733344200},
                "venue": {"id": 8560, "name": "Goodison Park", "city": "Liverpool"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 5,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 14",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": True,
                },
                "away": {
                    "id": 39,
                    "name": "Wolves",
                    "logo": "https://media.api-sports.io/football/teams/39.png",
                    "winner": False,
                },
            },
            "goals": {"home": 4, "away": 0},
            "score": {
                "halftime": {"home": 2, "away": 0},
                "fulltime": {"home": 4, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208174,
                "referee": "Craig Pawson, England",
                "timezone": "UTC",
                "date": "2024-12-14T15:00:00+00:00",
                "timestamp": 1734188400,
                "periods": {"first": 1734188400, "second": 1734192000},
                "venue": {"id": 494, "name": "Emirates Stadium", "city": "London"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 6,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 16",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 42,
                    "name": "Arsenal",
                    "logo": "https://media.api-sports.io/football/teams/42.png",
                    "winner": None,
                },
                "away": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": None,
                },
            },
            "goals": {"home": 0, "away": 0},
            "score": {
                "halftime": {"home": 0, "away": 0},
                "fulltime": {"home": 0, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208186,
                "referee": "Chris Kavanagh, England",
                "timezone": "UTC",
                "date": "2024-12-22T14:00:00+00:00",
                "timestamp": 1734876000,
                "periods": {"first": 1734876000, "second": 1734879600},
                "venue": {"id": 8560, "name": "Goodison Park", "city": "Liverpool"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 3,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 17",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": None,
                },
                "away": {
                    "id": 49,
                    "name": "Chelsea",
                    "logo": "https://media.api-sports.io/football/teams/49.png",
                    "winner": None,
                },
            },
            "goals": {"home": 0, "away": 0},
            "score": {
                "halftime": {"home": 0, "away": 0},
                "fulltime": {"home": 0, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208198,
                "referee": "Simon Hooper, England",
                "timezone": "UTC",
                "date": "2024-12-26T12:30:00+00:00",
                "timestamp": 1735216200,
                "periods": {"first": 1735216200, "second": 1735219800},
                "venue": {"id": 555, "name": "Etihad Stadium", "city": "Manchester"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 6,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 18",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 50,
                    "name": "Manchester City",
                    "logo": "https://media.api-sports.io/football/teams/50.png",
                    "winner": None,
                },
                "away": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": None,
                },
            },
            "goals": {"home": 1, "away": 1},
            "score": {
                "halftime": {"home": 1, "away": 1},
                "fulltime": {"home": 1, "away": 1},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208206,
                "referee": "Tony Harrington, England",
                "timezone": "UTC",
                "date": "2024-12-29T15:00:00+00:00",
                "timestamp": 1735484400,
                "periods": {"first": 1735484400, "second": 1735488000},
                "venue": {"id": 8560, "name": "Goodison Park", "city": "Liverpool"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 6,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 19",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": False,
                },
                "away": {
                    "id": 65,
                    "name": "Nottingham Forest",
                    "logo": "https://media.api-sports.io/football/teams/65.png",
                    "winner": True,
                },
            },
            "goals": {"home": 0, "away": 2},
            "score": {
                "halftime": {"home": 0, "away": 1},
                "fulltime": {"home": 0, "away": 2},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208213,
                "referee": "John Brooks, England",
                "timezone": "UTC",
                "date": "2025-01-04T15:00:00+00:00",
                "timestamp": 1736002800,
                "periods": {"first": 1736002800, "second": 1736006400},
                "venue": {
                    "id": 504,
                    "name": "Vitality Stadium",
                    "city": "Bournemouth, Dorset",
                },
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 4,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 20",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 35,
                    "name": "Bournemouth",
                    "logo": "https://media.api-sports.io/football/teams/35.png",
                    "winner": True,
                },
                "away": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": False,
                },
            },
            "goals": {"home": 1, "away": 0},
            "score": {
                "halftime": {"home": 0, "away": 0},
                "fulltime": {"home": 1, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208225,
                "referee": "Samuel Barrott, England",
                "timezone": "UTC",
                "date": "2025-01-15T19:30:00+00:00",
                "timestamp": 1736969400,
                "periods": {"first": 1736969400, "second": 1736973000},
                "venue": {"id": 8560, "name": "Goodison Park", "city": "Liverpool"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 6,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 21",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": False,
                },
                "away": {
                    "id": 66,
                    "name": "Aston Villa",
                    "logo": "https://media.api-sports.io/football/teams/66.png",
                    "winner": True,
                },
            },
            "goals": {"home": 0, "away": 1},
            "score": {
                "halftime": {"home": 0, "away": 0},
                "fulltime": {"home": 0, "away": 1},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208236,
                "referee": "Darren England, England",
                "timezone": "UTC",
                "date": "2025-01-19T14:00:00+00:00",
                "timestamp": 1737295200,
                "periods": {"first": 1737295200, "second": 1737298800},
                "venue": {"id": 8560, "name": "Goodison Park", "city": "Liverpool"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 6,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 22",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": True,
                },
                "away": {
                    "id": 47,
                    "name": "Tottenham",
                    "logo": "https://media.api-sports.io/football/teams/47.png",
                    "winner": False,
                },
            },
            "goals": {"home": 3, "away": 2},
            "score": {
                "halftime": {"home": 3, "away": 0},
                "fulltime": {"home": 3, "away": 2},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208245,
                "referee": "Tim Robinson, England",
                "timezone": "UTC",
                "date": "2025-01-25T15:00:00+00:00",
                "timestamp": 1737817200,
                "periods": {"first": 1737817200, "second": 1737820800},
                "venue": {
                    "id": 508,
                    "name": "American Express Stadium",
                    "city": "Falmer, East Sussex",
                },
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 10,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 23",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 51,
                    "name": "Brighton",
                    "logo": "https://media.api-sports.io/football/teams/51.png",
                    "winner": False,
                },
                "away": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": True,
                },
            },
            "goals": {"home": 0, "away": 1},
            "score": {
                "halftime": {"home": 0, "away": 1},
                "fulltime": {"home": 0, "away": 1},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
        {
            "fixture": {
                "id": 1208257,
                "referee": "Darren Bond, England",
                "timezone": "UTC",
                "date": "2025-02-01T15:00:00+00:00",
                "timestamp": 1738422000,
                "periods": {"first": 1738422000, "second": 1738425600},
                "venue": {"id": 8560, "name": "Goodison Park", "city": "Liverpool"},
                "status": {
                    "long": "Match Finished",
                    "short": "FT",
                    "elapsed": 90,
                    "extra": 5,
                },
            },
            "league": {
                "id": 39,
                "name": "Premier League",
                "country": "England",
                "logo": "https://media.api-sports.io/football/leagues/39.png",
                "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                "season": 2024,
                "round": "Regular Season - 24",
                "standings": True,
            },
            "teams": {
                "home": {
                    "id": 45,
                    "name": "Everton",
                    "logo": "https://media.api-sports.io/football/teams/45.png",
                    "winner": True,
                },
                "away": {
                    "id": 46,
                    "name": "Leicester",
                    "logo": "https://media.api-sports.io/football/teams/46.png",
                    "winner": False,
                },
            },
            "goals": {"home": 4, "away": 0},
            "score": {
                "halftime": {"home": 3, "away": 0},
                "fulltime": {"home": 4, "away": 0},
                "extratime": {"home": None, "away": None},
                "penalty": {"home": None, "away": None},
            },
        },
    ]


@pytest.fixture
def leagues_data():
    return {
        "get": "leagues",
        "parameters": {"team": "44"},
        "errors": [],
        "results": 6,
        "paging": {"current": 1, "total": 1},
        "response": [
            {
                "league": {
                    "id": 48,
                    "name": "League Cup",
                    "type": "Cup",
                    "logo": "https://media.api-sports.io/football/leagues/48.png",
                },
                "country": {
                    "name": "England",
                    "code": "GB-ENG",
                    "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                },
                "seasons": [
                    {
                        "year": 2022,
                        "start": "2022-08-02",
                        "end": "2023-02-26",
                        "current": False,
                        "coverage": {},
                    },
                    {
                        "year": 2023,
                        "start": "2023-08-08",
                        "end": "2024-02-25",
                        "current": False,
                        "coverage": {},
                    },
                    {
                        "year": 2024,
                        "start": "2024-08-13",
                        "end": "2025-02-06",
                        "current": True,
                        "coverage": {},
                    },
                ],
            },
            {
                "league": {
                    "id": 40,
                    "name": "Championship",
                    "type": "League",
                    "logo": "https://media.api-sports.io/football/leagues/40.png",
                },
                "country": {
                    "name": "England",
                    "code": "GB-ENG",
                    "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                },
                "seasons": [
                    {
                        "year": 2022,
                        "start": "2022-07-29",
                        "end": "2023-05-27",
                        "current": False,
                        "coverage": {},
                    },
                    {
                        "year": 2024,
                        "start": "2024-08-09",
                        "end": "2025-05-03",
                        "current": True,
                        "coverage": {},
                    },
                ],
            },
            {
                "league": {
                    "id": 45,
                    "name": "FA Cup",
                    "type": "Cup",
                    "logo": "https://media.api-sports.io/football/leagues/45.png",
                },
                "country": {
                    "name": "England",
                    "code": "GB-ENG",
                    "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                },
                "seasons": [
                    {
                        "year": 2021,
                        "start": "2021-08-06",
                        "end": "2022-05-14",
                        "current": False,
                        "coverage": {},
                    },
                    {
                        "year": 2022,
                        "start": "2022-08-05",
                        "end": "2023-06-03",
                        "current": False,
                        "coverage": {},
                    },
                    {
                        "year": 2023,
                        "start": "2023-08-04",
                        "end": "2024-05-25",
                        "current": False,
                        "coverage": {},
                    },
                    {
                        "year": 2024,
                        "start": "2024-08-02",
                        "end": "2025-02-08",
                        "current": True,
                        "coverage": {},
                    },
                ],
            },
            {
                "league": {
                    "id": 39,
                    "name": "Premier League",
                    "type": "League",
                    "logo": "https://media.api-sports.io/football/leagues/39.png",
                },
                "country": {
                    "name": "England",
                    "code": "GB-ENG",
                    "flag": "https://media.api-sports.io/flags/gb-eng.svg",
                },
                "seasons": [
                    {
                        "year": 2021,
                        "start": "2021-08-13",
                        "end": "2022-05-22",
                        "current": False,
                        "coverage": {},
                    },
                    {
                        "year": 2023,
                        "start": "2023-08-11",
                        "end": "2024-05-19",
                        "current": False,
                        "coverage": {},
                    },
                ],
            },
        ],
    }


@pytest.fixture
def standings_by_league_id_data():
    return {
        "get": "standings",
        "parameters": {"league": "39", "season": "2024"},
        "errors": [],
        "results": 1,
        "paging": {"current": 1, "total": 1},
        "response": [
            {
                "league": {
                    "id": 39,
                    "name": "Premier League",
                    "country": "England",
                    "season": 2024,
                    "standings": [
                        [
                            {
                                "rank": 1,
                                "team": {
                                    "id": 40,
                                    "name": "Liverpool",
                                },
                            },
                            {
                                "rank": 2,
                                "team": {
                                    "id": 42,
                                    "name": "Arsenal",
                                },
                            },
                            {
                                "rank": 3,
                                "team": {
                                    "id": 65,
                                    "name": "Nottingham Forest",
                                },
                            },
                            {
                                "rank": 4,
                                "team": {
                                    "id": 50,
                                    "name": "Manchester City",
                                },
                            },
                            {
                                "rank": 5,
                                "team": {
                                    "id": 35,
                                    "name": "Bournemouth",
                                },
                            },
                            {
                                "rank": 6,
                                "team": {
                                    "id": 49,
                                    "name": "Chelsea",
                                },
                            },
                            {
                                "rank": 7,
                                "team": {
                                    "id": 34,
                                    "name": "Newcastle",
                                },
                            },
                            {
                                "rank": 8,
                                "team": {
                                    "id": 36,
                                    "name": "Fulham",
                                },
                            },
                            {
                                "rank": 9,
                                "team": {
                                    "id": 66,
                                    "name": "Aston Villa",
                                },
                            },
                            {
                                "rank": 10,
                                "team": {
                                    "id": 51,
                                    "name": "Brighton",
                                },
                            },
                            {
                                "rank": 11,
                                "team": {
                                    "id": 55,
                                    "name": "Brentford",
                                },
                            },
                            {
                                "rank": 12,
                                "team": {
                                    "id": 47,
                                    "name": "Tottenham",
                                },
                            },
                            {
                                "rank": 13,
                                "team": {
                                    "id": 52,
                                    "name": "Crystal Palace",
                                },
                            },
                            {
                                "rank": 14,
                                "team": {
                                    "id": 45,
                                    "name": "Everton",
                                },
                            },
                            {
                                "rank": 15,
                                "team": {
                                    "id": 33,
                                    "name": "Manchester United",
                                },
                            },
                            {
                                "rank": 16,
                                "team": {
                                    "id": 48,
                                    "name": "West Ham",
                                },
                            },
                            {
                                "rank": 17,
                                "team": {
                                    "id": 39,
                                    "name": "Wolves",
                                },
                            },
                            {
                                "rank": 18,
                                "team": {
                                    "id": 57,
                                    "name": "Ipswich",
                                },
                            },
                            {
                                "rank": 19,
                                "team": {
                                    "id": 46,
                                    "name": "Leicester",
                                },
                            },
                            {
                                "rank": 20,
                                "team": {
                                    "id": 41,
                                    "name": "Southampton",
                                },
                            },
                        ]
                    ],
                }
            }
        ],
    }
