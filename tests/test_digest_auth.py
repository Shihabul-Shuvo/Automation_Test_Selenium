import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.digest_auth_page import DigestAuthPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_digest_auth_success(driver):
    page = DigestAuthPage(driver)
    page.navigate_to()
    assert "Digest Auth" in page.get_success_message()