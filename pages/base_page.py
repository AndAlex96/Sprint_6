from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

# метод помещен в бэйс, т.к. для работы обязательно прямое обращение к driver
    def assert_current_url_new_window(self, URL):
        current_window = self.driver.current_window_handle

        for window_handle in self.driver.window_handles:
            if window_handle != current_window:
                self.driver.switch_to.window(window_handle)
                break
        WebDriverWait(self.driver, 10).until(EC.url_to_be(URL))
        assert self.driver.current_url == URL

    def assert_current_url(self, URL):
        assert self.driver.current_url == URL
