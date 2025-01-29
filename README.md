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
