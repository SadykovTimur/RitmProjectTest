from selenium.webdriver.common.by import By

class ElementsLocarots:
    ELEMENTS = (By.XPATH, '(//div[@class="card mt-4 top-card"])[1]')
    CHECKBOX = (By.XPATH, '//span[contains(text(),"Check Box")]')
    BUTTON = (By.XPATH, '//button[@aria-label="Toggle"]')
    BUTTON1 = (By.XPATH, '(//button[@aria-label="Toggle"])[4]')
    WORDFILE = (By.XPATH, '//span[contains(text(),"Word File.doc")]')
    WORDFILE1 = (By.XPATH, '//span[contains(text(),"wordFile")]')

