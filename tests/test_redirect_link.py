import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.redirect_link_page import RedirectLinkPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_redirect_link(driver):
    page = RedirectLinkPage(driver)
    page.navigate_to()
    page.click_redirect_link()
    assert "status_codes/301" in page.get_current_url()