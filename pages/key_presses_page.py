from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class KeyPressesPage(BasePage):
    INPUT_FIELD = (By.ID, "target")
    RESULT = (By.ID, "result")  # Primary locator
    RESULT_FALLBACK = (By.XPATH, "//p[contains(text(), 'You entered')]")  # Fallback locator

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/key_presses")

    def press_key(self, key):
        element = self.find_element(*self.INPUT_FIELD)
        element.send_keys(key)
        self.driver.implicitly_wait(2)  # Add small delay for dynamic update

    def get_result_text(self):
        try:
            return self.find_element(*self.RESULT).text
        except:
            return self.find_element(*self.RESULT_FALLBACK).text