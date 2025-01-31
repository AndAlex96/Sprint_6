import pytest
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from pages.order_page import OrderPage
from pages.start_page import StartPage
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class TestOrderScooter:

    test_data = [['Андрей','Плотников','Королева 10','Черкизовская','88008008080'],
                 ['Иван','Иванов','Главная 10','Черкизовская','89009009090']]
# тест на создание заказа по кнопке Заказать в шапке
    @pytest.mark.parametrize('name, surname, address, metro_station, number_phone', test_data)
    def test_order_scooter_to_click_on_upper_button_order(self, driver, name, surname, address, metro_station, number_phone):

        start_page = StartPage(driver)
        order_page = OrderPage(driver)

        start_page.click_on_upper_button_order()
        order_page.filling_out_the_first_form(name, surname, address, metro_station, number_phone)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(OrderPageLocators.next_button))
        order_page.click_on_next_button()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.date_input))
        order_page.filling_out_the_second_form()
        WebDriverWait(driver, 5)
        order_page.click_on_order_button()
        order_page.click_on_yes_button()
        order_text = order_page.get_text_with_info_about_order()
        assert 'Заказ оформлен' in order_text

# тест на создание заказа по кнопке Заказать внизу страницы
    def test_order_scooter_to_click_on_bottom_button_order(self, driver):
        start_page = StartPage(driver)
        order_page = OrderPage(driver)

        start_page.click_on_bottom_button_order()
        order_page.filling_out_the_first_form()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(OrderPageLocators.next_button))
        order_page.click_on_next_button()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.date_input))
        order_page.filling_out_the_second_form()
        WebDriverWait(driver, 5)
        order_page.click_on_order_button()
        order_page.click_on_yes_button()
        order_text = order_page.get_text_with_info_about_order()
        assert 'Заказ оформлен' in order_text


class TestWorkLogoYaAndScooter():

    # тест на проверку открытия главной страницы Дзена по нажатию на логотип Яндекса
    def test_click_on_logo_ya_in_head(self, driver):
        base_page = BasePage(driver)
        start_page = StartPage(driver)
        order_page = OrderPage(driver)

        start_page.click_on_bottom_button_order()
        order_page.filling_out_the_first_form()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(OrderPageLocators.next_button))
        order_page.click_on_next_button()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.date_input))
        order_page.filling_out_the_second_form()
        WebDriverWait(driver, 5)
        order_page.click_on_order_button()
        order_page.click_on_yes_button()

        order_page.click_look_to_status_button()
        current_window = driver.current_window_handle

        base_page.click_on_logo_ya_in_head()
        for window_handle in driver.window_handles:
            if window_handle != current_window:
                driver.switch_to.window(window_handle)
                break
        WebDriverWait(driver, 10).until(EC.url_to_be('https://dzen.ru/?yredirect=true'))
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

    # тест на проверку открытия главной страницы сервиса при нажатии на логотип Самоката
    def test_click_on_logo_scooter_in_head(self, driver):
        base_page = BasePage(driver)
        start_page = StartPage(driver)
        order_page = OrderPage(driver)

        start_page.click_on_bottom_button_order()
        order_page.filling_out_the_first_form()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(OrderPageLocators.next_button))
        order_page.click_on_next_button()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(OrderPageLocators.date_input))
        order_page.filling_out_the_second_form()
        WebDriverWait(driver, 5)
        order_page.click_on_order_button()
        order_page.click_on_yes_button()

        order_page.click_look_to_status_button()
        base_page.click_on_logo_scooter_in_head()
        WebDriverWait(driver, 10).until(EC.url_to_be('https://qa-scooter.praktikum-services.ru/'))
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'