from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента с заданным ожиданием')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    @allure.step('Нажатие на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Получение текущего адреса в новом окне')
    def get_current_url_new_window(self, URL):
        current_window = self.driver.current_window_handle

        for window_handle in self.driver.window_handles:
            if window_handle != current_window:
                self.driver.switch_to.window(window_handle)
                break
        WebDriverWait(self.driver, 10).until(EC.url_to_be(URL))
        return self.driver.current_url

    @allure.step('Получение текущего адреса')
    def get_current_url(self):
        return self.driver.current_url
