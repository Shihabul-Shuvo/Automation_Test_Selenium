import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.checkboxes_page import CheckboxesPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_checkboxes_toggle(driver):
    page = CheckboxesPage(driver)
    page.navigate_to()
    # Toggle first checkbox and verify state
    initial_state = page.is_checkbox_selected(0)
    page.toggle_checkbox(0)
    assert page.is_checkbox_selected(0) != initial_state
    # Toggle second checkbox and verify state
    initial_state = page.is_checkbox_selected(1)
    page.toggle_checkbox(1)
    assert page.is_checkbox_selected(1) != initial_state