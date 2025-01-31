from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from locators.start_page_locators import StartPageLocators


class StartPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_upper_button_order(self):
        self.driver.find_element(*StartPageLocators.upper_button_order).click()
    def click_on_bottom_button_order(self):
        WebDriverWait(self.driver, 5)
        self.driver.find_element(*StartPageLocators.bottom_button_order).click()

    def click_on_question_button_1(self):
        self.driver.find_element(*StartPageLocators.question_button_1).click()
    def click_on_question_button_2(self):
        self.driver.find_element(*StartPageLocators.question_button_2).click()
    def click_on_question_button_3(self):
        self.driver.find_element(*StartPageLocators.question_button_3).click()
    def click_on_question_button_4(self):
        self.driver.find_element(*StartPageLocators.question_button_4).click()
    def click_on_question_button_5(self):
        self.driver.find_element(*StartPageLocators.question_button_5).click()
    def click_on_question_button_6(self):
        self.driver.find_element(*StartPageLocators.question_button_6).click()
    def click_on_question_button_7(self):
        self.driver.find_element(*StartPageLocators.question_button_7).click()
    def click_on_question_button_8(self):
        self.driver.find_element(*StartPageLocators.question_button_8).click()

    def get_text_from_answer_table_on_question_1(self):
        return self.driver.find_element(*StartPageLocators.answer_table_on_question_1).text
    def get_text_from_answer_table_on_question_2(self):
        return self.driver.find_element(*StartPageLocators.answer_table_on_question_2).text
    def get_text_from_answer_table_on_question_3(self):
        return self.driver.find_element(*StartPageLocators.answer_table_on_question_3).text
    def get_text_from_answer_table_on_question_4(self):
        return self.driver.find_element(*StartPageLocators.answer_table_on_question_4).text
    def get_text_from_answer_table_on_question_5(self):
        return self.driver.find_element(*StartPageLocators.answer_table_on_question_5).text
    def get_text_from_answer_table_on_question_6(self):
        return self.driver.find_element(*StartPageLocators.answer_table_on_question_6).text
    def get_text_from_answer_table_on_question_7(self):
        return self.driver.find_element(*StartPageLocators.answer_table_on_question_7).text
    def get_text_from_answer_table_on_question_8(self):
        return self.driver.find_element(*StartPageLocators.answer_table_on_question_8).text