from pages.start_page import StartPage


class TestImportantQuestionsOnStartPage:

    def test_of_opening_the_answer_to_1_question(self, driver):
        start_page = StartPage(driver)
        start_page.click_on_question_button_1()
        text_on_page = start_page.get_text_from_answer_table_on_question_1()
        assert 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.' in text_on_page

    def test_of_opening_the_answer_to_2_question(self, driver):
        start_page = StartPage(driver)
        start_page.click_on_question_button_2()
        text_on_page = start_page.get_text_from_answer_table_on_question_2()
        assert 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.' in text_on_page

    def test_of_opening_the_answer_to_3_question(self, driver):
        start_page = StartPage(driver)
        start_page.click_on_question_button_3()
        text_on_page = start_page.get_text_from_answer_table_on_question_3()
        assert 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.' in text_on_page

    def test_of_opening_the_answer_to_4_question(self, driver):
        start_page = StartPage(driver)
        start_page.click_on_question_button_4()
        text_on_page = start_page.get_text_from_answer_table_on_question_4()
        assert 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.' in text_on_page

    def test_of_opening_the_answer_to_5_question(self, driver):
        start_page = StartPage(driver)
        start_page.click_on_question_button_5()
        text_on_page = start_page.get_text_from_answer_table_on_question_5()
        assert 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.' in text_on_page

    def test_of_opening_the_answer_to_6_question(self, driver):
        start_page = StartPage(driver)
        start_page.click_on_question_button_6()
        text_on_page = start_page.get_text_from_answer_table_on_question_6()
        assert 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.' in text_on_page

    def test_of_opening_the_answer_to_7_question(self, driver):
        start_page = StartPage(driver)
        start_page.click_on_question_button_7()
        text_on_page = start_page.get_text_from_answer_table_on_question_7()
        assert 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.' in text_on_page

    def test_of_opening_the_answer_to_8_question(self, driver):
        start_page = StartPage(driver)
        start_page.click_on_question_button_8()
        text_on_page = start_page.get_text_from_answer_table_on_question_8()
        assert 'Да, обязательно. Всем самокатов! И Москве, и Московской области.' in text_on_page

