from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver



@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get('https://qa-scooter.praktikum-services.ru/')
    browser.find_element(By.ID, 'rcc-confirm-button').click() # закрываем окно с предупреждением о куках
    yield browser
    browser.quit()