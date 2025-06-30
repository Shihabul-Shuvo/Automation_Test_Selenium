from selenium.webdriver.common.by import By
from .base_page import BasePage

class MultipleWindowsPage(BasePage):
    LINK = (By.LINK_TEXT, "Click Here")
    NEW_WINDOW_TEXT = (By.CSS_SELECTOR, "div.example > h3")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/windows")

    def open_new_window(self):
        self.click(*self.LINK)

    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    def get_new_window_text(self):
        return self.find_element(*self.NEW_WINDOW_TEXT).text