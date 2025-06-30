from selenium.webdriver.common.by import By
from .base_page import BasePage

class RedirectLinkPage(BasePage):
    REDIRECT_LINK = (By.LINK_TEXT, "here")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/redirector")

    def click_redirect_link(self):
        self.click(*self.REDIRECT_LINK)

    def get_current_url(self):
        return self.driver.current_url