from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class DisappearingElementsPage(BasePage):
    GALLERY_LINK = (By.LINK_TEXT, "Gallery")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/disappearing_elements")

    def is_gallery_visible(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.GALLERY_LINK))
            return True
        except:
            return False

    def refresh_until_gallery_appears(self):
        for _ in range(5):  # Try up to 5 times
            if self.is_gallery_visible():
                return True
            self.driver.refresh()
        return False