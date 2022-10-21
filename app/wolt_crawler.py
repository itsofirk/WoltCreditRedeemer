from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from config import wolt_settings


opts = Options()
opts.headless = True
browser = Firefox(options=opts)


def perform_login(email):
    browser.get(wolt_settings.base_url)
    login_btn = find_login_button()


def find_login_button():
    login_buttons = browser.find_elements(By.XPATH, f'//button[text()="{wolt_settings.login_button_text}"]')
    if len(login_buttons) == 0:
        raise Exception('No matching buttons were found')
    if len(login_buttons) != 1:
        raise Exception(f'Found more than one button matching: {wolt_settings.login_button_text}')
    return login_buttons[0]

