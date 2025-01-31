from conftest import driver
from locators.base_page_locators import BasePageLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_logo_ya_in_head(self):
        self.driver.find_element(*BasePageLocators.logo_ya_in_head).click()

    def click_on_logo_scooter_in_head(self):
        self.driver.find_element(*BasePageLocators.logo_scooter_in_head).click()