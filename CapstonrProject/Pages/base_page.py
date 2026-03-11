from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from utilities.logger import get_logger
import time

logger = get_logger()


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        try:
            logger.info(f"Clicking element: {locator}")

            element = self.wait.until(EC.element_to_be_clickable(locator))

            # scroll element into view
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", element
            )

            try:
                element.click()
            except ElementClickInterceptedException:
                logger.warning("Normal click failed, trying JS click")
                self.driver.execute_script("arguments[0].click();", element)

        except TimeoutException:
            logger.error(f"Timeout: Element not clickable {locator}")
            raise

        except Exception as e:
            logger.error(f"Error clicking element {locator}: {e}")
            raise

    def send_keys(self, locator, text):
        try:
            logger.info(f"Sending keys '{text}' to element: {locator}")
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.send_keys(text)
            time.sleep(1)

        except TimeoutException:
            logger.error(f"Timeout: Element not visible {locator}")
            raise

        except NoSuchElementException:
            logger.error(f"Element not found {locator}")
            raise

        except Exception as e:
            logger.error(f"Error sending keys to {locator}: {e}")
            raise