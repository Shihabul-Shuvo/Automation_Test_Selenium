from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def login(self, username, password):
        self.send_keys(*self.USERNAME_INPUT, username)
        self.send_keys(*self.PASSWORD_INPUT, password)
        self.click(*self.SUBMIT_BUTTON)

    def get_flash_message(self):
        return self.find_element(*self.FLASH_MESSAGE).text