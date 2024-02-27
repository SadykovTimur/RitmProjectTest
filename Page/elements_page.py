from Page.base_page import BasePage
from Locators.elements_locators import ElementsLocators

class ElementsPage(BasePage):
    Locators = ElementsLocators

    def click_elements(self):
        self.element_is_clickable(self.Locators.ELEMENTS).click()
        self.element_is_clickable(self.Locators.CHECKBOX).click()
        self.element_is_clickable(self.Locators.BUTTON).click()
        self.element_is_clickable(self.Locators.BUTTON1).click()
        self.element_is_clickable(self.Locators.WORDFILE).click()

    def check_element(self):
        a = self.elements_are_present(self.Locators.WORDFILE1).text
        return a