import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.disappearing_elements_page import DisappearingElementsPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_disappearing_elements(driver):
    page = DisappearingElementsPage(driver)
    page.navigate_to()
    assert page.refresh_until_gallery_appears(), "Gallery link did not appear after 5 refreshes"