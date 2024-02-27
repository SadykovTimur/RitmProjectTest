from datetime import datetime
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    with allure.step("Get screenshot"):
        attach = driver.get_screenshot_as_png()
        allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type)
    driver.quit()