from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage

class ContextMenuPage(BasePage):
    HOT_SPOT = (By.ID, "hot-spot")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/context_menu")

    def right_click_hot_spot(self):
        element = self.find_element(*self.HOT_SPOT)
        ActionChains(self.driver).context_click(element).perform()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text