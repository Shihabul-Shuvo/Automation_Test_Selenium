import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_valid_login(driver):
    page = LoginPage(driver)
    page.navigate_to()
    page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in page.get_flash_message()

def test_invalid_username(driver):
    page = LoginPage(driver)
    page.navigate_to()
    page.login("invalid_user", "SuperSecretPassword!")
    assert "Your username is invalid!" in page.get_flash_message()

def test_invalid_password(driver):
    page = LoginPage(driver)
    page.navigate_to()
    page.login("tomsmith", "wrong_password")
    assert "Your password is invalid!" in page.get_flash_message()

def test_empty_fields(driver):
    page = LoginPage(driver)
    page.navigate_to()
    page.login("", "")
    assert "Your username is invalid!" in page.get_flash_message()

def test_ui_elements(driver):
    page = LoginPage(driver)
    page.navigate_to()
    username_field = page.find_element(*page.USERNAME_INPUT)
    password_field = page.find_element(*page.PASSWORD_INPUT)
    login_button = page.find_element(*page.SUBMIT_BUTTON)
    assert username_field.is_displayed() and username_field.is_enabled()
    assert password_field.is_displayed() and password_field.is_enabled()
    assert login_button.is_displayed() and login_button.is_enabled()