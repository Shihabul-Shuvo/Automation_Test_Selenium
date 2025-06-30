from selenium.webdriver.common.by import By
from .base_page import BasePage

class NotificationMessagesPage(BasePage):
    LINK = (By.LINK_TEXT, "Click here")
    FLASH = (By.ID, "flash")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/notification_message_rendered")

    def click_link(self):
        self.click(*self.LINK)

    def get_flash_message(self):
        return self.find_element(*self.FLASH).text