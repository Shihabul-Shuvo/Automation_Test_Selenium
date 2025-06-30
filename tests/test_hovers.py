import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.hovers_page import HoversPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_hovers(driver):
    page = HoversPage(driver)
    page.navigate_to()
    page.hover_over_figure(0)
    assert "user1" in page.get_user_name(0)