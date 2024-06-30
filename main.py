# Caminho: ./project/main.py

from config import EMAIL, PASSWORD
from data.cards import CARDS
from services.selenium_service import get_driver, SeleniumService


def main():
    with get_driver() as driver:
        selenium_service = SeleniumService(driver)
        selenium_service.login(EMAIL, PASSWORD)
        selenium_service.open_project_page()

        for card in CARDS:
            selenium_service.add_card(card)


if __name__ == "__main__":
    main()
