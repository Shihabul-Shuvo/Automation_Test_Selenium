from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckboxesPage(BasePage):
    CHECKBOXES = (By.CSS_SELECTOR, "input[type='checkbox']")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")

    def get_checkboxes(self):
        return self.find_elements(*self.CHECKBOXES)

    def toggle_checkbox(self, index):
        checkboxes = self.get_checkboxes()
        checkboxes[index].click()

    def is_checkbox_selected(self, index):
        return self.get_checkboxes()[index].is_selected()