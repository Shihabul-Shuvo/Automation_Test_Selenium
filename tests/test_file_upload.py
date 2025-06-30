import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.file_upload_page import FileUploadPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_file_upload(driver):
    page = FileUploadPage(driver)
    page.navigate_to()
    file_path = os.path.join(os.getcwd(), "test_file.txt")
    with open(file_path, "w") as f:
        f.write("Test content")
    page.upload_file(file_path)
    assert page.get_uploaded_file_name() == "test_file.txt"
    os.remove(file_path)