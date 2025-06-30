from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver():
    service = Service()  # Selenium Manager handles ChromeDriver
    driver = webdriver.Chrome(service=service)
    driver.get("https://the-internet.herokuapp.com/login")
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert "You logged into a secure area!" in driver.find_element(By.ID, "flash").text

def test_invalid_username(driver):
    driver.find_element(By.ID, "username").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert "Your username is invalid!" in driver.find_element(By.ID, "flash").text

def test_invalid_password(driver):
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert "Your password is invalid!" in driver.find_element(By.ID, "flash").text

def test_empty_fields(driver):
    driver.find_element(By.ID, "username").send_keys("")
    driver.find_element(By.ID, "password").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert "Your username is invalid!" in driver.find_element(By.ID, "flash").text

def test_ui_elements(driver):
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert username_field.is_displayed() and username_field.is_enabled()
    assert password_field.is_displayed() and password_field.is_enabled()
    assert login_button.is_displayed() and login_button.is_enabled()