import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.drag_drop_page import DragDropPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_drag_and_drop(driver):
    page = DragDropPage(driver)
    page.navigate_to()
    page.drag_a_to_b()
    assert page.get_column_b_text() == "A"