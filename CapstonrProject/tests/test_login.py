from Pages.login_page import LoginPage
from utilities.logger import get_logger
import time

logger = get_logger()


def test_user_login(setup):
    logger.info("Login test started")

    try:
        driver = setup
        login = LoginPage(driver)

        login.login()
        time.sleep(2)

        assert "bstackdemo" in driver.current_url
        logger.info("Login successful")

    except AssertionError as ae:
        logger.error(f"Assertion failed: {ae}")
        raise

    except Exception as e:
        logger.error(f"Test failed due to exception: {e}")
        raise

    finally:
        logger.info("Login test ended")

