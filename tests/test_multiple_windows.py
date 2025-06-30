import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.multiple_windows_page import MultipleWindowsPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_multiple_windows(driver):
    page = MultipleWindowsPage(driver)
    page.navigate_to()
    page.open_new_window()
    page.switch_to_new_window()
    assert "New Window" in page.get_new_window_text()