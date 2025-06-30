from selenium.webdriver.common.by import By
from .base_page import BasePage
import os

class FileUploadPage(BasePage):
    FILE_INPUT = (By.ID, "file-upload")
    SUBMIT_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILE = (By.ID, "uploaded-files")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/upload")

    def upload_file(self, file_path):
        self.send_keys(*self.FILE_INPUT, file_path)
        self.click(*self.SUBMIT_BUTTON)

    def get_uploaded_file_name(self):
        return self.find_element(*self.UPLOADED_FILE).text