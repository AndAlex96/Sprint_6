from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    def send_name_input(self, name):
        self.driver.find_element(*OrderPageLocators.name_input).send_keys(name)
    def send_surname_input(self, surname):
        self.driver.find_element(*OrderPageLocators.surname_input).send_keys(surname)
    def send_address_input(self, address):
        self.driver.find_element(*OrderPageLocators.address_input).send_keys(address)
    def send_metro_station_input(self, metro_station):
        self.driver.find_element(*OrderPageLocators.metro_station_input).click()
        self.driver.find_element(*OrderPageLocators.metro_station_input).send_keys(metro_station)
        self.driver.find_element(*OrderPageLocators.select_metro_station_input).click()
    def send_number_phone_input(self, number_phone):
        self.driver.find_element(*OrderPageLocators.number_phone_input).send_keys(number_phone)




    def filling_out_the_first_form(self, name='Андрей', surname='Плотников', address='Королева 10', metro_station='Черкизовская', number_phone='89209002020'): # заполнение первой формы сделали шагом
        self.send_name_input(name)
        self.send_surname_input(surname)
        self.send_address_input(address)
        self.send_metro_station_input(metro_station)
        self.send_number_phone_input(number_phone)

    def click_on_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()

    def send_date_input(self):
        self.driver.find_element(*OrderPageLocators.date_input).send_keys('01.02.2025')
        self.driver.find_element(*OrderPageLocators.date_input).send_keys(Keys.ENTER)
    def send_rental_period_input(self):
        self.driver.find_element(*OrderPageLocators.rental_period_input).click()
        WebDriverWait(self.driver, 5)
        self.driver.find_element(*OrderPageLocators.select_rental_period_input).click()

    def filling_out_the_second_form(self): # заполнение второй формы сделали шагом
        self.send_date_input()
        self.send_rental_period_input()

    def click_on_order_button(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()

    def click_on_yes_button(self):
        self.driver.find_element(*OrderPageLocators.yes_button).click()

    def get_text_with_info_about_order(self):
        return self.driver.find_element(*OrderPageLocators.window_info_about_order).text

    def click_look_to_status_button(self):
        self.driver.find_element(*OrderPageLocators.look_to_status_button).click()

