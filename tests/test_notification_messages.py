import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.notification_messages_page import NotificationMessagesPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_notification_messages(driver):
    page = NotificationMessagesPage(driver)
    page.navigate_to()
    page.click_link()
    message = page.get_flash_message()
    assert "Action successful" in message or "Action unsuccessful" in message