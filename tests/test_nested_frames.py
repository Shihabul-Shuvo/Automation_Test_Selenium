import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.nested_frames_page import NestedFramesPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_nested_frames(driver):
    page = NestedFramesPage(driver)
    page.navigate_to()
    page.switch_to_top_frame()
    page.switch_to_left_frame()
    assert "LEFT" in page.get_frame_text()