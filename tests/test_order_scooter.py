import allure
import pytest
from conftest import driver
from pages.order_page import OrderPage
from pages.start_page import StartPage
from locators.start_page_locators import StartPageLocators


@allure.title('Проверка создания заказа через кнопки Заказать в шапке главной страницы и внизу страницы')
@pytest.mark.parametrize('locator', [StartPageLocators.upper_button_order, StartPageLocators.bottom_button_order])
def test_order_scooter_to_click_on_upper_button_order(driver, locator):

    order_page = OrderPage(driver)
    start_page = StartPage(driver)

    start_page.click_on_button_order()
    order_page.filling_out_the_first_form('Андрей','Плотников','Королева 10','Черкизовская','88008008080')
    order_page.click_on_next_button()
    order_page.filling_out_the_second_form()
    order_page.click_on_order_button()
    order_page.click_on_yes_button()
    order_text = order_page.get_text_with_info_about_order()
    assert 'Заказ оформлен' in order_text
