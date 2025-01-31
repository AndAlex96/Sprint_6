from selenium.webdriver.common.by import By

class OrderPageLocators:
    name_input = [By.CSS_SELECTOR, "input[placeholder='* Имя']"]
    surname_input = [By.CSS_SELECTOR, "input[placeholder='* Фамилия']"]
    address_input = [By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"]
    metro_station_input = [By.CSS_SELECTOR, "input[placeholder='* Станция метро']"]
    select_metro_station_input = [By.XPATH, './/div[@class="select-search__select"]'] # строка раскрывающегося списка
    number_phone_input = [By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"]

    next_button = [By.XPATH, '//button[text()="Далее"]']  # кнопка Далее после первой формы

    date_input = [By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"]
    rental_period_input = [By.XPATH, ".//div[text()='* Срок аренды']"]
    select_rental_period_input = [By.XPATH, "//div[text()='сутки']"] # строка Сутки из выпадающего списка

    order_button = [By.XPATH, '//button[2][text()="Заказать"]']  # кнопка Заказать после второй формы
    yes_button = [By.XPATH, '//button[text()="Да"]'] # кнопка Да в окне подтверждения заказа

    window_info_about_order = [By.XPATH, "//div[text()='Заказ оформлен']"]

    look_to_status_button = [By.XPATH, '//button[text()="Посмотреть статус"]']