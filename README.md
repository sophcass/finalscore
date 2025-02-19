# finalscore
A powerful football score prediction system that generates accurate forecasts for upcoming games

## Livescore Build-Up Game Web Scraper
This web scraper automates interactions with the Livescore Build-Up game, helping users gain a competitive edge by analysing submitted scores and identifying unpicked ones. By choosing less common scores, users increase their chances of winning if the score occurs in the game.

### Usage
1. Ensure ChromeDriver is installed and accessible. See https://developer.chrome.com/docs/chromedriver/downloads.  
2. Create a Livescore account if you don't have one already.
3. Set environment variables for your Livescore login:  
    ```bash
    export LOGIN_USERNAME="your_username"
    export LOGIN_PASSWORD="your_password"
    ```
4. Run the script:
    ```bash
    python livescore_scraper.py
    ```
5. View the frequency table to identify unpicked scores.

> **Note:** ChromeDriver and environment variables must be properly configured for the scraper to work.

## Football Team Performance Metrics
This script retrieves and calculates various performance metrics for a football team within a given league. The key metrics include:
* League position
* Number of fixtures played
* Win percentage
* Average goals scored per match
* Average goals conceded per match
* Recent form index (based on last 5 matches)

### Usage
1. Create an API-Football account if you don't have one already.
2. Set environment variables for your API-Football API key:
    ```bash
    export RAPIDAPI_KEY="your_api_key"
    ```
3. Run the script with the following command-line arguments:
    ```bash
    python team_performance.py --league "Premier League" --team "Everton" --country "England"
    ```
The arguments:
* league: The league name (e.g., "Premier League") (Required)
* team: The team name (e.g., "Everton") (Required)
* country: The country the team is from (e.g., "England") (Optional)

### Example Output
```bash
Everton is 10 in the Premier League
10 fixtures played in the Premier League by Everton

Win percentage is: 50.0 
Avg goals scored are: 1.5 
Average conceded goals are: 1.2 
Recent form index is 2.8
```
