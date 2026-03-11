# tests/test_checkout.py
import pytest
from Pages.checkout_page import CheckoutPage
from utilities.test_helpers import login_and_add_to_cart
from utilities.excel_utils import get_checkout_data
from utilities.logger import get_logger
import time

logger = get_logger()

# Load checkout data once
CHECKOUT_DATA = get_checkout_data("C:/Users/KIIT/Desktop/CapstonrProject/testdata/checkout_data.xlsx")

@pytest.mark.parametrize("details", CHECKOUT_DATA)
def test_complete_checkout(setup, details):
    logger.info("Checkout test started")

    driver = setup

    try:
        cart = login_and_add_to_cart(driver)
        time.sleep(1)

        cart.click_checkout()
        time.sleep(1)

        checkout = CheckoutPage(driver)
        checkout.fill_details(details)
        time.sleep(2)

        assert checkout.is_confirmation_displayed(), "Confirmation message not shown after checkout"
        logger.info("Checkout completed successfully")

    except AssertionError as ae:
        logger.error(f"Assertion failed: {ae}")
        raise

    except Exception as e:
        logger.error(f"Checkout test failed due to exception: {e}")
        raise

    finally:
        logger.info("Checkout test ended")

