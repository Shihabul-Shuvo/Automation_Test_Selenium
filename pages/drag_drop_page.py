from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage

class DragDropPage(BasePage):
    COLUMN_A = (By.ID, "column-a")
    COLUMN_B = (By.ID, "column-b")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    def drag_a_to_b(self):
        source = self.find_element(*self.COLUMN_A)
        target = self.find_element(*self.COLUMN_B)
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    def get_column_b_text(self):
        return self.find_element(*self.COLUMN_B).text