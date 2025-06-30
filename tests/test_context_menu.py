import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.context_menu_page import ContextMenuPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_context_menu_alert(driver):
    page = ContextMenuPage(driver)
    page.navigate_to()
    page.right_click_hot_spot()
    assert page.get_alert_text() == "You selected a context menu"