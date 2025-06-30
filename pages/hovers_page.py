from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage

class HoversPage(BasePage):
    FIGURES = (By.CLASS_NAME, "figure")
    USER_NAME = (By.CSS_SELECTOR, "div.figure > div > h5")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/hovers")

    def hover_over_figure(self, index):
        figures = self.find_elements(*self.FIGURES)
        ActionChains(self.driver).move_to_element(figures[index]).perform()

    def get_user_name(self, index):
        return self.find_elements(*self.USER_NAME)[index].text