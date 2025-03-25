from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get('https://qa-scooter.praktikum-services.ru/')
    browser.find_element(By.ID, 'rcc-confirm-button').click() # закрываем окно с предупреждением о куках
    yield browser
    browser.quit()