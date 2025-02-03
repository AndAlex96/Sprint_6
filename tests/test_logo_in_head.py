from conftest import driver
from pages.order_page import OrderPage
from pages.start_page import StartPage
import allure
from start_page_locators import StartPageLocators


class TestWorkLogoYaAndScooter:

    @allure.title('Проверка открытия главной страницы Дзена по нажатию на логотип Яндекса')
    def test_click_on_logo_ya_in_head(self, driver):
        order_page = OrderPage(driver)
        start_page = StartPage(driver)

        start_page.click_on_button_order(locator=StartPageLocators.upper_button_order)
        order_page.filling_out_the_first_form('Андрей', 'Плотников', 'Королева 10', 'Черкизовская', '88008008080')
        order_page.click_on_next_button()
        order_page.filling_out_the_second_form()
        order_page.click_on_order_button()
        order_page.click_on_yes_button()

        order_page.click_look_to_status_button()

        order_page.click_on_logo_ya_in_head()
        order_page.assert_current_url_new_window(URL='https://dzen.ru/?yredirect=true')

    @allure.title('Проверка открытия главной страницы сервиса при нажатии на логотип Самоката')
    def test_click_on_logo_scooter_in_head(self, driver):
        start_page = StartPage(driver)
        order_page = OrderPage(driver)

        start_page.click_on_button_order(locator=StartPageLocators.upper_button_order)
        order_page.filling_out_the_first_form('Андрей', 'Плотников', 'Королева 10', 'Черкизовская', '88008008080')
        order_page.click_on_next_button()
        order_page.filling_out_the_second_form()
        order_page.click_on_order_button()
        order_page.click_on_yes_button()

        order_page.click_look_to_status_button()
        order_page.click_on_logo_scooter_in_head()
        order_page.assert_current_url(URL='https://qa-scooter.praktikum-services.ru/')
