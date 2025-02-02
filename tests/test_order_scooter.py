import allure

from conftest import driver
from pages.order_page import OrderPage
from pages.start_page import StartPage


class TestOrderScooter:

    # тест на создание заказа по кнопке Заказать в шапке
    @allure.title('Проверка создания заказа через кнопку в шапке главной страницы')
    def test_order_scooter_to_click_on_upper_button_order(self, driver):

        order_page = OrderPage(driver)
        start_page = StartPage(driver)
        start_page.click_on_upper_button_order()
        order_page.filling_out_the_first_form('Андрей','Плотников','Королева 10','Черкизовская','88008008080')
        order_page.click_on_next_button()
        order_page.filling_out_the_second_form()
        order_page.click_on_order_button()
        order_page.click_on_yes_button()
        order_text = order_page.get_text_with_info_about_order()
        assert 'Заказ оформлен' in order_text

# тест на создание заказа по кнопке Заказать внизу страницы
    @allure.title('Проверка создания заказа через кнопку Заказать в нижней части главной страницы')
    def test_order_scooter_to_click_on_bottom_button_order(self, driver):
        start_page = StartPage(driver)
        order_page = OrderPage(driver)

        start_page.click_on_bottom_button_order()
        order_page.filling_out_the_first_form('Андрей','Плотников','Королева 10','Черкизовская','88008008080')
        order_page.click_on_next_button()
        order_page.filling_out_the_second_form()
        order_page.click_on_order_button()
        order_page.click_on_yes_button()
        order_text = order_page.get_text_with_info_about_order()
        assert 'Заказ оформлен' in order_text