from common_objects import *
from common_strings import *

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
import chromedriver_autoinstaller
from pytest import mark
import os
import random
import string

browser_driver = Driver()
test_settings = TestSettings()


def start_test(user_type=UserData.STANDARD_USER, browser=Browsers.CHROME, url=URLs.SAUCE_DEMO, logging=True):
    """
    Starts the test execution based on the browser & url provided

    :param user_type: The user type of the user to use with the test
    :param browser: The browser to use for testing
    :param url: The url to use for testing
    :param logging: The logging to use for testing
    """
    if browser == Browsers.CHROME:
        chromedriver_autoinstaller.install()
        browser_driver.set_driver(webdriver.Chrome())
    elif browser == Browsers.FIREFOX:
        browser_driver.set_driver(webdriver.Firefox())
    else:
        os.system("killall 'Safari'")
        browser_driver.set_driver(webdriver.Safari())

    test_settings.set_test_settings(user_type=user_type, browser=browser, url=url, logging=logging)
    browser_driver.driver.get(url)


def start_test_and_sign_in(user_type=UserData.STANDARD_USER, browser=Browsers.CHROME,
                           url=URLs.SAUCE_DEMO, logging=True):
    """
    Starts the test execution based on the browser & url provided

    :param user_type: The user type of the user to sign in with
    :param browser: The browser to use for testing
    :param url: The url to use for testing
    :param logging: The logging to use for testing
    """

    start_test(user_type=user_type, browser=browser, url=url, logging=logging)

    # Login
    send_keys(LoginPage.USERNAME_FIELD, user_type)
    send_keys(LoginPage.PASSWORD_FIELD, UserData.PASSWORD)
    press_button(LoginPage.LOGIN_BUTTON)


def press_button(button_id, button_type=By.ID, iteration=0, text="", timeout=30, child_path="", wait=False) -> str:
    """
    Presses the button based on the id passed in
    :param button_id: The id of the button to press
    :param button_type: The type of the button to press
    :param iteration: The iteration of the button to press
    :param text: The text of the button to press
    :param timeout: The time to wait to find the button
    :param child_path: The child path of the field element
    :param wait: If True, waits a second after clicking
    :return: text
    """
    log(f"press_button - button_id: {button_id}, button_type: {button_type}, "
        f"iteration: {iteration}, text: {text}, timeout: {timeout}")

    # Auto-set button type if list
    if isinstance(button_id, list):
        button_id = "//" + button_id[0] + "[@" + button_id[1] + "='" + button_id[2] + "']" + child_path
        button_type = By.XPATH

    try:
        button_to_press = WebDriverWait(browser_driver.get_driver(), timeout).until(
            ec.presence_of_all_elements_located((button_type, button_id)))
    except TimeoutException:
        log(f"Unable to find element: {button_id}", severity=1)
    else:
        if text:  # Find by text
            text_list = []
            for button in button_to_press:
                if button.get_attribute('innerText') == text:
                    text_list.append(button)
            text_list[iteration].click()
        else:  # Find by iteration
            button_to_press[iteration].click()

        if wait:
            sleep(5)
        return text


def send_keys(field_id, text, field_type=By.ID, iteration=0, timeout=30, child_path="") -> str:
    """
    Presses the button based on the id passed in
    :param field_id: The id of the field to send keys to
    :param text: The text to send to the field
    :param field_type: The type of the field to send keys to
    :param iteration: The iteration of the field to send keys to
    :param timeout: The time to wait to find the field
    :param child_path: The child path of the field element
    :return: text
    """
    log(f"send_keys - field_id: {field_id}, field_type: {field_type}, "
        f"iteration: {iteration}, text: {text}, timeout: {timeout}, child_path: {child_path}")

    # Auto-set field type if list
    if isinstance(field_id, list):
        field_id = "//" + field_id[0] + "[@" + field_id[1] + "='" + field_id[2] + "']" + child_path
        field_type = By.XPATH

    try:
        field = WebDriverWait(browser_driver.get_driver(), timeout).until(
            ec.presence_of_all_elements_located((field_type, field_id)))
    except TimeoutException:
        log(f"Unable to find element: {field_id}", severity=1)
    else:
        field[iteration].send_keys(text)
        return text


def check_for_element(element_id, element_type=By.ID, child_path="", timeout=5, text="") -> bool:
    log(f"check_for_element - element_id: {element_id}, element_type: {element_type}, "
        f"text: {text}, timeout: {timeout}, child_path: {child_path}")

    # Auto-set field type if list
    if isinstance(element_id, list):
        element_id = "//" + element_id[0] + "[@" + element_id[1] + "='" + element_id[2] + "']" + child_path
        element_type = By.XPATH

    try:
        WebDriverWait(browser_driver.get_driver(), timeout).until(
            ec.presence_of_all_elements_located((element_type, element_id)))
        return True
    except TimeoutException:
        return False


def assign_element(element_id, element_type=By.ID, child_path="", timeout=5, text="", iteration=0):
    """
    Assigns the element based on the id and type given

    :param element_id: The id of the element to assign
    :param element_type: The type of the element to assign
    :param child_path: The child path of the element to assign
    :param timeout: The timeout to find the element to assign
    :param text: The text of the element to find
    :param iteration: The iteration of the element to assign
    :return: element
    """
    log(f"assign_element - element_id: {element_id}, element_type: {element_type}, "
        f"text: {text}, timeout: {timeout}, child_path: {child_path}, iteration: {iteration}")

    # Auto-set field type if list
    if isinstance(element_id, list):
        element_id = "//" + element_id[0] + "[@" + element_id[1] + "='" + element_id[2] + "']" + child_path
        element_type = By.XPATH

    try:
        elements = WebDriverWait(browser_driver.get_driver(), timeout).until(
            ec.presence_of_all_elements_located((element_type, element_id)))
    except TimeoutException:
        log(f"Unable to assign element: {element_id}", severity=1)
    else:
        if text:  # Find by text
            text_list = []
            for element in elements:
                if element.get_attribute('innerText') == text:
                    text_list.append(element)
            return text_list[iteration]
        else:  # Find by iteration
            return elements[iteration]


def assign_elements(element_id, element_type=By.ID, child_path="", timeout=5, text=""):
    """
    Assigns the elements based on the id and type given

    :param element_id: The id of the elements to assign
    :param element_type: The type of the elements to assign
    :param child_path: The child path of the elements to assign
    :param timeout: The timeout to find the elements to assign
    :param text: The text of the elements to find
    :return: elements
    """
    log(f"assign_elements - element_id: {element_id}, element_type: {element_type}, "
        f"text: {text}, timeout: {timeout}, child_path: {child_path}")

    # Auto-set field type if list
    if isinstance(element_id, list):
        element_id = "//" + element_id[0] + "[@" + element_id[1] + "='" + element_id[2] + "']" + child_path
        element_type = By.XPATH

    try:
        elements = WebDriverWait(browser_driver.get_driver(), timeout).until(
            ec.presence_of_all_elements_located((element_type, element_id)))
    except TimeoutException:
        log(f"Unable to assign element: {element_id}", severity=1)
    else:
        if text:  # Find by text
            text_list = []
            for element in elements:
                if element.get_attribute('innerText') == text:
                    text_list.append(element)
            return text_list
        else:
            return elements


def log(message, severity=0):
    """
    Logs the message to the console based on the message and severity

    :param message: The message to log
    :param severity: The severity of the message
    """

    if test_settings.logging:
        if severity == 0:
            print(f"LOG: {message}")
        elif severity == 1:
            print(f"ERROR: {message}")
            raise Exception(f"ERROR: {message}")


def get_element_text(element_id, element_type=By.ID, child_path="", timeout=5, text="", iteration=0) -> str:
    """

    :param element_id: The id of the element to assign
    :param element_type: The type of the element to assign
    :param child_path: The child path of the element to assign
    :param timeout: The timeout to find the element to assign
    :param text: The text of the element to find
    :param iteration: The iteration of the element to assign
    :return: str
    """

    element = assign_element(element_id=element_id, element_type=element_type, child_path=child_path,
                             timeout=timeout, text=text, iteration=iteration)

    return element.get_attribute('innerText')


def get_random_string(length=5) -> str:
    """
    Returns a random string with the length provided
    :return: str
    """

    return ''.join(random.choices(string.ascii_lowercase, k=length))
