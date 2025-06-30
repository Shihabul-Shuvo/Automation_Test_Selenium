import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.horizontal_slider_page import HorizontalSliderPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_horizontal_slider(driver):
    page = HorizontalSliderPage(driver)
    page.navigate_to()
    page.move_slider(50)  # Move slider to the right
    assert float(page.get_slider_value()) > 0