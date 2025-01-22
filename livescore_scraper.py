import json
import os
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import (
    TimeoutException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

START_URL = "https://www.livescore.com/en/football-games/build-up/"


def _set_up_browser() -> WebDriver:
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/79.0.3945.79 Safari/537.36 "
    )

    service = Service(executable_path="/usr/local/bin/chromedriver", port=9515)

    driver = webdriver.Chrome(service=service, options=options)

    return driver


def _login(driver: WebDriver):
    login_xpath = "//div[@data-testid='bb-game-login-button']"
    login_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, login_xpath))
    )
    login_btn.click()
    login_btn.click()

    username = os.getenv("LOGIN_USERNAME")
    password = os.getenv("LOGIN_PASSWORD")
    if not username or not password:
        raise Exception(
            "Please set your username and password in your environmental variables"
        )
    sleep(2)

    email_xpath = "//input[@name='email']"
    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, email_xpath))
        )
    except TimeoutException:
        login_btn.click()
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, email_xpath))
        )
    password_xpath = "//input[@name='password']"
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, password_xpath))
    )

    email_input.send_keys(username)
    password_input.send_keys(password)

    login_xpath = "//button[@data-testid='login-form_contact-submit-button']"
    login_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, login_xpath))
    )
    login_btn.click()

    # Save cookies after logging in
    cookies = driver.get_cookies()
    with open("cookies.json", "w") as file:
        json.dump(cookies, file)


def get_this_weeks_scores_submitted(driver: WebDriver) -> dict[str, int]:
    leaderboard_items_xpath = "//div[contains(@data-testid, 'leaderboard-item')]"
    leaderboard_items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, leaderboard_items_xpath))
    )
    scores_submitted: dict[str, int] = {}
    for item in leaderboard_items:
        item.click()

        scores_xpath = "//p[contains(text(), 'The final score will be')]"
        scores = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, scores_xpath))
        )
        if len(scores) > 1:
            raise Exception("There should only be one score visible!")

        score = scores[0].text.split()[-1]
        scores_submitted = update_counter(scores_submitted, score)

        item.click()

    return scores_submitted


def update_counter(dictionary: dict[str, int], key: str) -> dict[str, int]:
    if key in dictionary:
        dictionary[key] += 1
    else:
        dictionary[key] = 1
    return dictionary


def get_leaderboard_scores():
    driver: WebDriver = _set_up_browser()
    try:
        driver.get(START_URL)

        # # Load cookies in a new session
        # with open("cookies.json", "r") as file:
        #     cookies = json.load(file)
        # for cookie in cookies:
        #     driver.add_cookie(cookie)

        accept_cookies_id = "onetrust-accept-btn-handler"
        accept_cookies_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, accept_cookies_id))
        )
        accept_cookies_btn.click()
        age_gate_xpath = "//button[@data-testid='ageGating_adult-button']"
        age_gate_btn = driver.find_element(By.XPATH, age_gate_xpath)
        age_gate_btn.click()
        _login(driver=driver)

        # Wait for the iframe to load
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//iframe[@data-testid='bet-builder_iframe']")
            )
        )
        driver.switch_to.frame(iframe)

        leaderboard_xpath = "//a[@href='/build-up/leaderboard']"
        leaderboard_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, leaderboard_xpath))
        )
        leaderboard_btn.click()

        scores_submitted = get_this_weeks_scores_submitted(driver=driver)

        print(f"The frequency of scores submitted are: {scores_submitted}")

        # Switch back to the main page
        driver.switch_to.default_content()

    finally:
        driver.quit()


if __name__ == "__main__":
    get_leaderboard_scores()
