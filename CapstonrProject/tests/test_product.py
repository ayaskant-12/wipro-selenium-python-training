from utilities.test_helpers import login_and_add_to_cart
from utilities.logger import get_logger
import time

logger = get_logger()

def test_add_product(setup):
    logger.info("Add product test started")

    try:
        driver = setup

        login_and_add_to_cart(driver)
        time.sleep(2)

        assert "checkout" not in driver.current_url
        logger.info("Product added successfully")

    except AssertionError as ae:
        logger.error(f"Assertion failed: {ae}")
        raise

    except Exception as e:
        logger.error(f"Test failed due to exception: {e}")
        raise

    finally:
        logger.info("Add product test ended")

