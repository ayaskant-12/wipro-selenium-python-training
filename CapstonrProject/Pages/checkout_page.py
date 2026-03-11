# Pages/checkout_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from utilities.logger import get_logger
import time

logger = get_logger()

class CheckoutPage(BasePage):
    first_name = (By.ID, "firstNameInput")
    last_name = (By.ID, "lastNameInput")
    address = (By.ID, "addressLine1Input")
    state = (By.ID, "provinceInput")
    postal = (By.ID, "postCodeInput")
    submit = (By.ID, "checkout-shipping-continue")
    confirmation_message = (By.ID, "confirmation-message")

    def fill_details(self, details):
        """
        details: dict with keys 'first_name', 'last_name', 'address', 'state', 'postal'
        """
        logger.info("Filling checkout details")
        self.send_keys(self.first_name, details['first_name'])
        time.sleep(1)
        self.send_keys(self.last_name, details['last_name'])
        time.sleep(1)
        self.send_keys(self.address, details['address'])
        time.sleep(1)
        self.send_keys(self.state, details['state'])
        time.sleep(1)
        self.send_keys(self.postal, details['postal'])
        time.sleep(1)
        logger.info("Submitting checkout form")
        self.click(self.submit)
        time.sleep(1)

    def is_confirmation_displayed(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.confirmation_message))
            logger.info("Confirmation message is displayed")
            return True
        except Exception as e:
            logger.error(f"Confirmation message not displayed: {e}")
            return False