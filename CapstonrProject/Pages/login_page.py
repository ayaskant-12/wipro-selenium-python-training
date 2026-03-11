from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from utilities.logger import get_logger
import time


logger = get_logger()


class LoginPage(BasePage):

    sign_in_btn = (By.ID, "signin")

    username_dropdown = (By.ID, "react-select-2-input")
    password_dropdown = (By.ID, "react-select-3-input")

    login_button = (By.ID, "login-btn")

    def login(self):
        try:
            logger.info("Click Sign In button")
            self.click(self.sign_in_btn)

            logger.info("Wait until login modal appears")
            self.wait.until(
                EC.visibility_of_element_located(self.username_dropdown)
            )

            logger.info("Enter Username")
            username_field = self.driver.find_element(*self.username_dropdown)
            username_field.send_keys("demouser")
            username_field.send_keys("\n")
            time.sleep(1)

            logger.info("Enter Password")
            password_field = self.driver.find_element(*self.password_dropdown)
            password_field.send_keys("testingisfun99")
            password_field.send_keys("\n")
            time.sleep(1)

            logger.info("Click Login")
            self.click(self.login_button)

        except Exception as e:
            logger.error(f"Login failed: {e}")
            raise