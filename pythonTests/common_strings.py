class URLs:
    SAUCE_DEMO = "https://www.saucedemo.com/"


class Browsers:
    CHROME = "chrome"
    FIREFOX = "firefox"
    SAFARI = "safari"


class LoginPage:
    USERNAME_FIELD = "user-name"
    PASSWORD_FIELD = "password"
    LOGIN_BUTTON = "login-button"
    ERROR_MESSAGE = ["h3", "data-test", "error"]
    LOCKED_OUT_ERROR_MESSAGE = "Epic sadface: Sorry, this user has been locked out."
    USERNAME_REQUIRED_MESSAGE = "Epic sadface: Username is required"
    PASSWORD_REQUIRED_MESSAGE = "Epic sadface: Password is required"
    USERNAME_PASSWORD_MISMATCH_MESSAGE = "Epic sadface: Username and password do not match any user in this service"


class UserData:
    STANDARD_USER = "standard_user"
    LOCKED_OUT_USER = "locked_out_user"
    PROBLEM_USER = "problem_user"
    PERFORMANCE_GLITCH_USER = "performance_glitch_user"

    PASSWORD = "secret_sauce"


class InventoryPage:
    BACK_TO_PRODUCTIONS_BUTTON = "back-to-products"
    MENU_BUTTON = ["div", "class", "bm-burger-button"]
    LOGOUT_BUTTON = "logout_sidebar_link"
    SHOPPING_CART_CONTAINER = ["div", "id", "shopping_cart_container"]

    SORT_CONTAINER = ["select", "data-test", "product_sort_container"]
    A_TO_Z_OPTION = ["option", "value", "az"]
    Z_TO_A_OPTION = ["option", "value", "za"]
    LOW_TO_HIGH_PRICE_OPTION = ["option", "value", "lohi"]
    HIGH_TO_LOW_PRICE_OPTION = ["option", "value", "hilo"]

    INVENTORY_ITEM_NAME = ["div", "class", "inventory_item_name"]
    INVENTORY_ITEM_DESC = ["div", "class", "inventory_item_desc"]
    INVENTORY_ITEM_PRICE = ["div", "class", "inventory_item_price"]
    INVENTORY_ITEM_IMAGE = ["div", "class", "inventory_item_img"]

    ADD_BACKPACK_TO_CART = "add-to-cart-sauce-labs-backpack"
    ADD_BIKE_LIGHT_TO_CART = "add-to-cart-sauce-labs-bike-light"
    ADD_BOLT_TSHIRT_TO_CART = "add-to-cart-sauce-labs-bolt-t-shirt"
    ADD_FLEECE_JACKET_TO_CART = "add-to-cart-sauce-labs-fleece-jacket"
    ADD_ONESIE_TO_CART = "add-to-cart-sauce-labs-onesie"
    ADD_RED_TSHIRT_TO_CART = "add-to-cart-test.allthethings()-t-shirt-(red)"

    SAUCE_LABS_BACKPACK = "Sauce Labs Backpack"
    SAUCE_LABS_BIKE_LIGHT = "Sauce Labs Bike Light"
    SAUCE_LABS_BOLT_TSHIRT = "Sauce Labs Bolt T-Shirt"
    SAUCE_LABS_FLEECE_JACKET = "Sauce Labs Fleece Jacket"
    SAUCE_LABS_ONESIE = "Sauce Labs Onesie"
    TEST_ALL_THE_THINGS_TSHIRT_RED = "Test.allTheThings() T-Shirt (Red)"


class CartPage:
    CONTINUE_SHOPPING_BUTTON = "continue-shopping"
    CHECKOUT_BUTTON = "checkout"

    INVENTORY_ITEM_NAME = ["div", "class", "inventory_item_name"]

    FIRST_NAME_FIELD = "first-name"
    LAST_NAME_FIELD = "last-name"
    ZIP_FIELD = "postal-code"
    CANCEL_BUTTON = "cancel"
    CONTINUE_BUTTON = "continue"
    FINISH_BUTTON = "finish"

    CONFIRMATION_CONTAINER = "checkout_complete_container"


class FooterPage:
    SOCIAL_TWITTER = ["li", "class", "social_twitter"]
    TWITTER_URL = "https://twitter.com/saucelabs"
    SOCIAL_FACEBOOK = ["li", "class", "social_facebook"]
    FACEBOOK_URL = "https://www.facebook.com/saucelabs"
    SOCIAL_LINKEDIN = ["li", "class", "social_linkedin"]
    LINKEDIN_URL = "https://www.linkedin.com/company/sauce-labs/"

