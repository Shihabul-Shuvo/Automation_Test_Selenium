import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.forgot_password_page import ForgotPasswordPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_forgot_password(driver):
    page = ForgotPasswordPage(driver)
    page.navigate_to()
    page.submit_email("test@example.com")
    assert "Your e-mail's been sent!" in page.get_success_message()