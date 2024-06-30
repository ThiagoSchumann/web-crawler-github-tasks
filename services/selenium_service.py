# Caminho: ./project/services/selenium_service.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from contextlib import contextmanager
import time
from config import DRIVER_PATH, GITHUB_LOGIN_URL, PROJECT_URL


@contextmanager
def get_driver():
    driver = webdriver.Chrome(service=Service(executable_path=DRIVER_PATH))
    try:
        yield driver
    finally:
        driver.quit()


class SeleniumService:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.get(GITHUB_LOGIN_URL)
        time.sleep(1)

        email_field = self.driver.find_element(By.ID, "login_field")
        email_field.send_keys(email)

        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.NAME, "commit")
        login_button.click()
        time.sleep(1)

    def open_project_page(self):
        self.driver.get(PROJECT_URL)
        time.sleep(1)

    def add_card(self, card):
        add_item_button = self.driver.find_element(
            By.XPATH, '//*[@id="f75ad846"]/button')
        add_item_button.click()
        time.sleep(1)

        title_field = self.driver.find_element(
            By.XPATH, '//*[@id="combobox-input-1"]')
        title_field.send_keys(card["title"])
        title_field.send_keys(Keys.RETURN)
        time.sleep(1)

        elemento = self.driver.find_element(
            By.XPATH, f'//*[contains(text(), "{card["title"]}")]')
        elemento.click()
        time.sleep(1)

        button_edit = self.driver.find_element(
            By.XPATH, '//*[@id="__primerPortalRoot__"]/div[6]/div/div[2]/div[2]/div/div/div[1]/div/section/article/header/button')
        button_edit.click()
        time.sleep(1)

        text_area = self.driver.find_element(
            By.XPATH, '//textarea[@placeholder="Leave a comment"]')
        text_area.click()
        text_area.send_keys(card["description"])
        text_area.send_keys(Keys.RETURN)
        text_area.send_keys(card["checklist"])
        time.sleep(1)

        update_comment = self.driver.find_element(
            By.XPATH, '//span[@data-component="text" and text()="Update comment"]')
        update_comment.click()
        time.sleep(1)

        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
