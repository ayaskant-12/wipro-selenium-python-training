# utilities/test_helpers.py

from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.cart_page import CartPage
from utilities.logger import get_logger

logger = get_logger()


def login_and_add_to_cart(driver):
    """Log in, add the first product to cart, and navigate to cart page."""

    try:
        logger.info("Starting login and add to cart helper")

        login_page = LoginPage(driver)
        login_page.login()

        home = HomePage(driver)
        home.add_product_to_cart()
        home.go_to_cart()

        logger.info("Product successfully added and navigated to cart")

        return CartPage(driver)

    except Exception as e:
        logger.error(f"Error in login_and_add_to_cart helper: {e}")
        raise


