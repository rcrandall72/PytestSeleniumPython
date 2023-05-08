from common_functions import *
from common_strings import *


@mark.regression
class TestSauceDemo:
    @staticmethod
    @mark.smoke
    def test_login_logout(browser):
        """
        Tests a user can successfully log in and out of the app
        """
        # Start test and sign in
        start_test_and_sign_in(browser=browser)

        # Logout of app
        press_button(InventoryPage.MENU_BUTTON, wait=True)
        press_button(InventoryPage.LOGOUT_BUTTON)

        # Assert user is logged out and back on login page
        assert check_for_element(LoginPage.LOGIN_BUTTON)
        assert browser_driver.get_driver().current_url == URLs.SAUCE_DEMO

    @staticmethod
    def test_login_with_locked_user(browser):
        """
        Tests a user cannot successfully log in with a locked user
        """
        # Start test and sign in
        start_test_and_sign_in(user_type=UserData.LOCKED_OUT_USER, browser=browser)

        # Check user is not signed in and has correct error message
        assert check_for_element(LoginPage.ERROR_MESSAGE)
        assert get_element_text(LoginPage.ERROR_MESSAGE) == LoginPage.LOCKED_OUT_ERROR_MESSAGE

    @staticmethod
    def test_user_signing_credential_errors(browser):
        """
        Tests a user must provide good credentials in order to log in
        """
        # Start Test
        start_test(browser=browser)

        # Test Error message with no credentials
        press_button(LoginPage.LOGIN_BUTTON)
        assert check_for_element(LoginPage.ERROR_MESSAGE)
        assert get_element_text(LoginPage.ERROR_MESSAGE) == LoginPage.USERNAME_REQUIRED_MESSAGE

        # Test Error message with only username
        send_keys(LoginPage.USERNAME_FIELD, get_random_string())
        press_button(LoginPage.LOGIN_BUTTON)
        assert check_for_element(LoginPage.ERROR_MESSAGE)
        assert get_element_text(LoginPage.ERROR_MESSAGE) == LoginPage.PASSWORD_REQUIRED_MESSAGE

        # Test Error message with bad username & password
        send_keys(LoginPage.PASSWORD_FIELD, get_random_string())
        press_button(LoginPage.LOGIN_BUTTON)
        assert check_for_element(LoginPage.ERROR_MESSAGE)
        assert get_element_text(LoginPage.ERROR_MESSAGE) == LoginPage.USERNAME_PASSWORD_MISMATCH_MESSAGE

    @staticmethod
    @mark.smoke
    def test_buy_item(browser):
        """
        Tests a user can successfully buy an item
        """
        # Start test and sign in
        start_test_and_sign_in(browser=browser)

        # Add item to cart
        press_button(InventoryPage.ADD_BACKPACK_TO_CART)
        assert get_element_text(InventoryPage.SHOPPING_CART_CONTAINER) == "1"

        # Open cart and check we have the right item
        press_button(InventoryPage.SHOPPING_CART_CONTAINER)
        assert get_element_text(CartPage.INVENTORY_ITEM_NAME) == InventoryPage.SAUCE_LABS_BACKPACK

        # Continue to finalize purchase
        press_button(CartPage.CHECKOUT_BUTTON)
        send_keys(CartPage.FIRST_NAME_FIELD, get_random_string())
        send_keys(CartPage.LAST_NAME_FIELD, get_random_string())
        send_keys(CartPage.ZIP_FIELD, get_random_string())
        press_button(CartPage.CONTINUE_BUTTON)
        press_button(CartPage.FINISH_BUTTON)

        # Assert completion
        assert check_for_element(CartPage.CONFIRMATION_CONTAINER)

    @staticmethod
    def test_social_media_links(browser):
        """
        Tests the social media links route correctly
        """
        # Start test and sign in
        start_test_and_sign_in(browser=browser)

        # Open Twitter link
        press_button(FooterPage.SOCIAL_TWITTER, wait=True)
        if test_settings.browser == Browsers.CHROME:
            browser_driver.driver.switch_to.window(browser_driver.driver.window_handles[-1])
        else:
            browser_driver.driver.switch_to.window(browser_driver.driver.window_handles[1])
        assert browser_driver.driver.current_url == FooterPage.TWITTER_URL

        # Open Facebook
        browser_driver.driver.switch_to.window(browser_driver.driver.window_handles[0])
        press_button(FooterPage.SOCIAL_FACEBOOK, wait=True)
        if test_settings.browser == Browsers.CHROME:
            browser_driver.driver.switch_to.window(browser_driver.driver.window_handles[-1])
        else:
            browser_driver.driver.switch_to.window(browser_driver.driver.window_handles[1])
        assert browser_driver.driver.current_url == FooterPage.FACEBOOK_URL

        # Open LinkedIn
        browser_driver.driver.switch_to.window(browser_driver.driver.window_handles[0])
        press_button(FooterPage.SOCIAL_LINKEDIN, wait=True)
        if test_settings.browser == Browsers.CHROME:
            browser_driver.driver.switch_to.window(browser_driver.driver.window_handles[-1])
        else:
            browser_driver.driver.switch_to.window(browser_driver.driver.window_handles[1])
        assert FooterPage.LINKEDIN_URL in browser_driver.driver.current_url

    @staticmethod
    def test_sort_products(browser):
        """
        Verifies that products can be sorted in order
        """
        # Start test and sign in
        start_test_and_sign_in(browser=browser)

        # Sort products by A to Z
        press_button(InventoryPage.SORT_CONTAINER)
        press_button(InventoryPage.A_TO_Z_OPTION)
        item_names = assign_elements(InventoryPage.INVENTORY_ITEM_NAME)
        for i in range(0, len(item_names)-1):
            assert item_names[i].get_attribute('innerText') < item_names[i+1].get_attribute('innerText')

        # Sort products by A to Z
        press_button(InventoryPage.SORT_CONTAINER)
        press_button(InventoryPage.Z_TO_A_OPTION)
        item_names = assign_elements(InventoryPage.INVENTORY_ITEM_NAME)
        for i in range(0, len(item_names)-1):
            assert item_names[i].get_attribute('innerText') > item_names[i+1].get_attribute('innerText')

        # Sort products by low to high
        press_button(InventoryPage.SORT_CONTAINER)
        press_button(InventoryPage.LOW_TO_HIGH_PRICE_OPTION)
        item_prices = assign_elements(InventoryPage.INVENTORY_ITEM_PRICE)
        for i in range(0, len(item_prices)-1):
            assert float(item_prices[i].get_attribute('innerText')[1:])\
                   <= float(item_prices[i+1].get_attribute('innerText')[1:])

        # Sort products by high to low
        press_button(InventoryPage.SORT_CONTAINER)
        press_button(InventoryPage.HIGH_TO_LOW_PRICE_OPTION)
        item_prices = assign_elements(InventoryPage.INVENTORY_ITEM_PRICE)
        for i in range(0, len(item_prices)-1):
            assert float(item_prices[i].get_attribute('innerText')[1:])\
                   >= float(item_prices[i+1].get_attribute('innerText')[1:])
