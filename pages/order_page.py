from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
import allure
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Нажимаем на Яндекс в логотипе')
    def click_on_logo_ya_in_head(self):
        self.click_on_element(locator=OrderPageLocators.logo_ya_in_head)

    @allure.step('Нажимаем на скутер в логотипе')
    def click_on_logo_scooter_in_head(self):
        self.click_on_element(locator=OrderPageLocators.logo_scooter_in_head)

    @allure.step('Вводим имя')
    def send_name_input(self, name):
        self.find_element(locator=OrderPageLocators.name_input).send_keys(name)

    @allure.step('Вводим фамилию')
    def send_surname_input(self, surname):
        self.find_element(locator=OrderPageLocators.surname_input).send_keys(surname)

    @allure.step('Вводим адрес')
    def send_address_input(self, address):
        self.find_element(locator=OrderPageLocators.address_input).send_keys(address)

    @allure.step('Выбираем станцию метро')
    def send_metro_station_input(self, metro_station):
        self.click_on_element(locator=OrderPageLocators.metro_station_input)
        self.find_element(locator=OrderPageLocators.metro_station_input).send_keys(metro_station)
        self.click_on_element(locator=OrderPageLocators.select_metro_station_input)

    @allure.step('Вводим номер телефона')
    def send_number_phone_input(self, number_phone):
        self.find_element(locator=OrderPageLocators.number_phone_input).send_keys(number_phone)

# сделали шагом заполнение перовой формы
    @allure.step('Шаг - заполнение первой формы заказа')
    def filling_out_the_first_form(self, name='Андрей', surname='Плотников', address='Королева 10', metro_station='Черкизовская', number_phone='89209002020'): # заполнение первой формы сделали шагом
        self.send_name_input(name)
        self.send_surname_input(surname)
        self.send_address_input(address)
        self.send_metro_station_input(metro_station)
        self.send_number_phone_input(number_phone)

    @allure.step('Нажимаем на кнопку Далее')
    def click_on_next_button(self):
        self.click_on_element(locator=OrderPageLocators.next_button)

    @allure.step('Выбираем дату заказа')
    def send_date_input(self):
        self.find_element(locator=OrderPageLocators.date_input).send_keys('01.02.2025')
        self.find_element(locator=OrderPageLocators.date_input).send_keys(Keys.ENTER)

    @allure.step('Выбираем срок аренды')
    def send_rental_period_input(self):
        self.click_on_element(locator=OrderPageLocators.rental_period_input)
        self.click_on_element(locator=OrderPageLocators.select_rental_period_input)

    @allure.step('Шаг - заполнение второй страницы формы заказа')
    def filling_out_the_second_form(self): # заполнение второй формы сделали шагом
        self.send_date_input()
        self.send_rental_period_input()

    @allure.step('Нажимаем на Заказать в форме заказа')
    def click_on_order_button(self):
        self.click_on_element(locator=OrderPageLocators.order_button)

    @allure.step('Нажимаем Да для подтверждения создания заказа')
    def click_on_yes_button(self):
        self.click_on_element(locator=OrderPageLocators.yes_button)

    @allure.step('Получаем текст о создании заказа')
    def get_text_with_info_about_order(self):
        return self.find_element(locator=OrderPageLocators.window_info_about_order).text

    @allure.step('Нажимаем на кнопку получения подробных данных о заказе')
    def click_look_to_status_button(self):
        self.click_on_element(locator=OrderPageLocators.look_to_status_button)

