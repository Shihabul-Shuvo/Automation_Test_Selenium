from selenium.webdriver.common.by import By
from .base_page import BasePage

class ForgotPasswordPage(BasePage):
    EMAIL_INPUT = (By.ID, "email")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.ID, "content")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/forgot_password")

    def submit_email(self, email):
        self.send_keys(*self.EMAIL_INPUT, email)
        self.click(*self.SUBMIT_BUTTON)

    def get_success_message(self):
        return self.find_element(*self.SUCCESS_MESSAGE).text