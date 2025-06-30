from selenium.webdriver.common.by import By
from .base_page import BasePage

class DigestAuthPage(BasePage):
    def navigate_to(self):
        self.driver.get("https://admin:admin@the-internet.herokuapp.com/digest_auth")

    def get_success_message(self):
        return self.find_element(By.TAG_NAME, "h3").text