from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from utilities.logger import get_logger
import time

logger = get_logger()

class HomePage(BasePage):

    first_product = (By.XPATH, "(//div[@class='shelf-item'])[1]")
    add_to_cart_btn = (By.XPATH, "(//div[@class='shelf-item']//div[text()='Add to cart'])[1]")
    cart_icon = (By.CLASS_NAME, "bag")

    def add_product_to_cart(self):
        try:
            logger.info("Adding first product to cart")
            self.click(self.add_to_cart_btn)
            time.sleep(1)

        except Exception as e:
            logger.error(f"Failed to add product to cart: {e}")
            raise

    def go_to_cart(self):
        try:
            logger.info("Navigating to cart")
            self.click(self.cart_icon)
            time.sleep(1)

        except Exception as e:
            logger.error(f"Failed to navigate to cart: {e}")
            raise