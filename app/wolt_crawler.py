import logging
from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import wolt_settings

logger = logging.getLogger(__name__)
opts = Options()
opts.add_argument("--headless")
opts.add_argument("--start-maximized")
opts.add_argument('user-data-dir=' + wolt_settings.edge_user_data)
opts.add_argument('user-profile=Default')
opts.add_argument("--disable-extensions")  # disabling extensions
opts.add_argument("--no-sandbox")  # Bypass OS security model
browser = Edge(options=opts)


def until_wrapper(f, *args, **kwargs):
    def wrap(driver):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            logger.exception(e)
            return False
    return wrap


def _find_elem(pattern) -> WebElement:
    login_buttons = browser.find_elements(By.XPATH, pattern)
    if len(login_buttons) == 0:
        raise Exception('No matching buttons were found')
    if len(login_buttons) != 1:
        raise Exception(f'Found more than one button matching')
    return login_buttons[0]


def perform_login(email):
    logger.info("Loading wolt homepage...")
    browser.get(wolt_settings.base_url)
    wrapper = until_wrapper(find_elem_by_text, wolt_settings.show_login_form_button_text, tag='button')
    login_btn = WebDriverWait(browser, 5)\
        .until(wrapper)
    try:
        find_elem_by_text("Accept") \
            .click()
    except Exception as e:
        logger.exception(e)
    logger.debug("Showing login form")
    # find_elem_by_text(wolt_settings.show_login_form_button_text, tag='button') \
    #     .click()
    login_btn.click()
    logger.debug("Typing email address")
    browser.find_element(By.ID, wolt_settings.email_input_id) \
        .send_keys(email)
    logger.info("Logging in...")
    find_elem_by_text(wolt_settings.send_email_button_text, 'div') \
        .click()


def find_elem_by_text(inner_text, tag='*') -> WebElement:
    return _find_elem(f'//{tag}[text()="{inner_text}"]')


def find_elem_by_placeholder(inner_text, tag='*') -> WebElement:
    return _find_elem(f'//{tag}[@placeholder="{inner_text}"]')


def redeem_code(code):
    if wolt_settings.redeem_path not in browser.current_url:
        browser.get(wolt_settings.base_url + wolt_settings.redeem_path)
    else:
        sleep(2)
    find_elem_by_placeholder(wolt_settings.promo_code_hint)\
        .send_keys(code)
    _btn = _find_elem(f'//div[text()="{wolt_settings.redeem_button_text}"]/..')
    print("redeeming "+ str(code))
    if _btn.tag_name != 'button':
        raise TypeError("Couldn't find a button element")
    _btn.click()
    print("redeemed " + str(code))

