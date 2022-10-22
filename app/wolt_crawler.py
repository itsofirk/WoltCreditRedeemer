import logging

from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from config import wolt_settings

logger = logging.getLogger(__name__)
opts = Options()
opts.add_argument("--headless")
opts.add_argument("--incognito")
opts.add_argument("--start-maximized")
browser = Edge(options=opts)


def perform_login(email):
    logger.info("Loading wolt homepage...")
    browser.get(wolt_settings.base_url)
    find_any_by_text("Accept") \
        .click()
    logger.debug("Showing login form")
    find_button_by_text(wolt_settings.show_login_form_button_text) \
        .click()
    logger.debug("Typing email address")
    browser.find_element(By.ID, wolt_settings.email_input_id) \
        .send_keys(email)
    logger.info("Logging in...")
    find_any_by_text(wolt_settings.send_email_button_text, 'div') \
        .click()


def find_any_by_text(inner_text, tag='*') -> WebElement:
    login_buttons = browser.find_elements(By.XPATH, f'//{tag}[text()="{inner_text}"]')
    if len(login_buttons) == 0:
        raise Exception('No matching buttons were found')
    if len(login_buttons) != 1:
        raise Exception(f'Found more than one button matching: {inner_text}')
    return login_buttons[0]


def find_button_by_text(inner_text) -> WebElement:
    login_buttons = browser.find_elements(By.XPATH, f'//button[text()="{inner_text}"]')
    if len(login_buttons) == 0:
        raise Exception('No matching buttons were found')
    if len(login_buttons) != 1:
        raise Exception(f'Found more than one button matching: {inner_text}')
    return login_buttons[0]
