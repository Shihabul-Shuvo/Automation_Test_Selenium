from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class KeyPressesPage(BasePage):
    INPUT_FIELD = (By.ID, "target")
    RESULT = (By.ID, "result")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/key_presses")

    def press_key(self, key):
        self.send_keys(*self.INPUT_FIELD, key)

    def get_result_text(self):
        return self.find_element(*self.RESULT).text