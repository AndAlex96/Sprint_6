from locators.start_page_locators import StartPageLocators
from pages.base_page import BasePage
import allure

class StartPage(BasePage):

    @allure.step('')
    def click_on_upper_button_order(self):
        self.click_on_element(locator=StartPageLocators.upper_button_order)

    @allure.step('')
    def click_on_bottom_button_order(self):
        self.click_on_element(locator=StartPageLocators.bottom_button_order)

    @allure.step('Нажимаем на вопрос в разделе Вопросы о важном')
    def click_on_question_button(self, number_question_button):

        if number_question_button == 1:
            locator = StartPageLocators.question_button_1
        elif number_question_button == 2:
            locator = StartPageLocators.question_button_2
        elif number_question_button == 3:
            locator = StartPageLocators.question_button_3
        elif number_question_button == 4:
            locator = StartPageLocators.question_button_4
        elif number_question_button == 5:
            locator = StartPageLocators.question_button_5
        elif number_question_button == 6:
            locator = StartPageLocators.question_button_6
        elif number_question_button == 7:
            locator = StartPageLocators.question_button_7
        elif number_question_button == 8:
            locator = StartPageLocators.question_button_8
        else:
            raise ValueError("Номер вопроса должен быть от 1 до 8")
        return self.click_on_element(locator)

    @allure.step('Получаем текст ответа на вопрос в разделе Вопросы о важном')
    def get_text_from_answer_table(self, question_number):

        if question_number == 1:
            locator = StartPageLocators.answer_table_on_question_1
        elif question_number == 2:
            locator = StartPageLocators.answer_table_on_question_2
        elif question_number == 3:
            locator = StartPageLocators.answer_table_on_question_3
        elif question_number == 4:
            locator = StartPageLocators.answer_table_on_question_4
        elif question_number == 5:
            locator = StartPageLocators.answer_table_on_question_5
        elif question_number == 6:
            locator = StartPageLocators.answer_table_on_question_6
        elif question_number == 7:
            locator = StartPageLocators.answer_table_on_question_7
        elif question_number == 8:
            locator = StartPageLocators.answer_table_on_question_8
        else:
            raise ValueError("Номер вопроса должен быть от 1 до 8")

        return self.find_element(locator).text