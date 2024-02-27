from Page.elements_page import ElementsPage
from conftest import driver


class TestElements:

    def test_elements(self, driver):
        page = ElementsPage(driver, "https://demoqa.com/")
        page.open()
        page.click_elements()
        check_text = page.check_element()
        assert check_text == "wordFile"
        print("Test successful")
