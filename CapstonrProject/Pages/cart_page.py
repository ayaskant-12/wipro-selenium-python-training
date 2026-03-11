from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from utilities.logger import get_logger
import time

logger = get_logger()

class CartPage(BasePage):

    checkout_btn = (By.XPATH, "//div[text()='Checkout']")

    def click_checkout(self):
        try:
            logger.info("Clicking checkout button")
            self.click(self.checkout_btn)

        except Exception as e:
            logger.error(f"Checkout button click failed: {e}")
            raise