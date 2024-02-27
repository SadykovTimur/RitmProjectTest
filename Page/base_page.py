from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

#Нужен тогда когда необходимо чтобы элемент был видимым
    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

# Нужен не один элемент а несколько
    def elements_are_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

# Позволяет найти элемент в DOM-элементе(дереве), DevTools
    def element_is_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

# Позволяет найти несколько элементов в DOM-элементе(дереве), DevTools
    def elements_are_present(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

# Поиск невидимых элементов
    def element_is_not_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

# Проверить кликабельный ли элемент
    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

# Скролл страницы
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
