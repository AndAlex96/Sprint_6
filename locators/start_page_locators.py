from selenium.webdriver.common.by import By

class StartPageLocators:
    upper_button_order = [By.CLASS_NAME, 'Button_Button__ra12g']  # верхняя кнопка Заказать - в шапке страницы
    bottom_button_order = [By.XPATH,'//div[5]/button[text()="Заказать"]']  # кнопка Заказать в нижней части страницы

    question_button_1 = [By.ID, 'accordion__heading-0']  # Сколько это стоит
    question_button_2 = [By.ID, 'accordion__heading-1']  # Хочу сразу несколько самокатов
    question_button_3 = [By.ID, 'accordion__heading-2']  # Как рассчитать время аренды
    question_button_4 = [By.ID, 'accordion__heading-3']  # Можно ли заказать самокат прямо на сегодня
    question_button_5 = [By.ID, 'accordion__heading-4']  # Можно ли продлить заказ или вернуть самокат раньше
    question_button_6 = [By.ID, 'accordion__heading-5']  # Вы привозите зарядку вместе с самокатом
    question_button_7 = [By.ID, 'accordion__heading-6']  # Можно ли отменить заказ
    question_button_8 = [By.ID, 'accordion__heading-7']  # Я живу за МКАДом, привезете

    answer_table_on_question_1 = [By.ID, 'accordion__panel-0']  # текст ответа на вопрос - сколько это стоит
    answer_table_on_question_2 = [By.ID, 'accordion__panel-1']  # текст ответа на вопрос - Хочу сразу несколько самокатов
    answer_table_on_question_3 = [By.ID, 'accordion__panel-2']  # текст ответа на вопрос - Как рассчитать время аренды
    answer_table_on_question_4 = [By.ID, 'accordion__panel-3']  # текст ответа на вопрос - Можно ли заказать самокат прямо на сегодня
    answer_table_on_question_5 = [By.ID, 'accordion__panel-4']  # текст ответа на вопрос - Можно ли продлить заказ или вернуть самокат раньше
    answer_table_on_question_6 = [By.ID, 'accordion__panel-5']  # текст ответа на вопрос - Вы привозите зарядку вместе с самокатом
    answer_table_on_question_7 = [By.ID, 'accordion__panel-6']  # текст ответа на вопрос - Можно ли отменить заказ
    answer_table_on_question_8 = [By.ID, 'accordion__panel-7']  # текст ответа на вопрос - Я живу за МКАДом, привезете