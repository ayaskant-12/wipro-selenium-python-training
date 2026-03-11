import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#
#     yield driver
#     driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox"
    )





# screenshot hook  taking if  the test case fails
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = (
                item.funcargs.get("driver") or
                item.funcargs.get("setup") or
                item.funcargs.get("browser")
        )
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)
        else:
            print("No driver found in funcargs")


# @pytest.fixture(scope="function")
# def driver():
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Remote(
#         command_executor="http://localhost:4444",
#         options=options
#     )
#     yield driver
#     driver.quit()

#
# @pytest.fixture(scope="function")
# def setup():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     driver.get("https://bstackdemo.com/")
#     yield driver
#     driver.quit()

@pytest.fixture(scope="function")
def setup(request):

    browser = request.config.getoption("--browser")

    if browser.lower() == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )

    else:
        raise Exception("Browser not supported: choose chrome or firefox")

    driver.maximize_window()
    driver.get("https://bstackdemo.com/")

    yield driver
    driver.quit()