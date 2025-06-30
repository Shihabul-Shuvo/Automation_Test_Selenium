from selenium.webdriver.common.by import By
from .base_page import BasePage
import os
import time

class FileDownloadPage(BasePage):
    FILE_LINK = (By.LINK_TEXT, "some-file.txt")

    def navigate_to(self):
        self.driver.get("https://the-internet.herokuapp.com/download")

    def download_file(self):
        self.click(*self.FILE_LINK)

    def is_file_downloaded(self, download_dir, filename="some-file.txt"):
        time.sleep(2)  # Wait for download to complete
        return os.path.exists(os.path.join(download_dir, filename))