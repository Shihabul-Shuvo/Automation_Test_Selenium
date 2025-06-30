from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage

class HorizontalSliderPage(BasePage):
    SLIDER = (By.CSS_SELECTOR, "input[type='range']")
    VALUE = (By.ID, "range")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/horizontal_slider")

    def move_slider(self, offset):
        slider = self.find_element(*self.SLIDER)
        ActionChains(self.driver).click_and_hold(slider).move_by_offset(offset, 0).release().perform()

    def get_slider_value(self):
        return self.find_element(*self.VALUE).text