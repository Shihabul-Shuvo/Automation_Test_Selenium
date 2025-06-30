from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class DropdownPage(BasePage):
    DROPDOWN = (By.ID, "dropdown")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/dropdown")

    def select_option_by_text(self, text):
        select = Select(self.find_element(*self.DROPDOWN))
        select.select_by_visible_text(text)

    def select_option_by_value(self, value):
        select = Select(self.find_element(*self.DROPDOWN))
        select.select_by_value(value)

    def select_option_by_index(self, index):
        select = Select(self.find_element(*self.DROPDOWN))
        select.select_by_index(index)

    def get_selected_option_text(self):
        select = Select(self.find_element(*self.DROPDOWN))
        return select.first_selected_option.text