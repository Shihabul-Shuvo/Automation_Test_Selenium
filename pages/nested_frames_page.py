from selenium.webdriver.common.by import By
from .base_page import BasePage

class NestedFramesPage(BasePage):
    TOP_FRAME = (By.NAME, "frame-top")
    LEFT_FRAME = (By.NAME, "frame-left")
    FRAME_TEXT = (By.TAG_NAME, "body")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/nested_frames")

    def switch_to_top_frame(self):
        self.driver.switch_to.frame(self.find_element(*self.TOP_FRAME))

    def switch_to_left_frame(self):
        self.driver.switch_to.frame(self.find_element(*self.LEFT_FRAME))

    def get_frame_text(self):
        return self.find_element(*self.FRAME_TEXT).text