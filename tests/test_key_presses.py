import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.key_presses_page import KeyPressesPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_key_presses(driver):
    page = KeyPressesPage(driver)
    page.navigate_to()
    page.press_key(Keys.ENTER)
    assert "You entered: ENTER" in page.get_result_text()