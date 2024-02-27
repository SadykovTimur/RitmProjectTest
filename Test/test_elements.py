import allure
from Page.elements_page import ElementsPage
from conftest import driver


@allure.feature('TestElements')
class TestElements:
    @allure.title('test_elements')
    def test_elements(self, driver):
        with allure.step('Open web site'):
            page = ElementsPage(driver, "https://demoqa.com/")
        page.open()
        page.click_elements()
        check_text = page.check_element()
        with allure.step('Checking'):
            assert check_text == "wordFile"
            print("Test successful")
