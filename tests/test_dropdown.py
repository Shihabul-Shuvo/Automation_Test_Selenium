import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.dropdown_page import DropdownPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_dropdown_selection(driver):
    page = DropdownPage(driver)
    page.navigate_to()
    page.select_option_by_text("Option 1")
    assert page.get_selected_option_text() == "Option 1"
    page.select_option_by_value("2")
    assert page.get_selected_option_text() == "Option 2"
    page.select_option_by_index(1)
    assert page.get_selected_option_text() == "Option 1"