from urls_credits import Urls
import pytest
from selenium import webdriver
from main_page import MainPage

class TestFaq:

    driver = None

    @classmethod
    def setup_class(cls):
  #       создали драйвер для браузера
        cls.driver = webdriver.Firefox()



    @pytest.mark.parametrize("n, expected", [(MainPage.QUESTION_1, MainPage.ANSWER_1),
                                         (MainPage.QUESTION_2, MainPage.ANSWER_2),
                                         (MainPage.QUESTION_3, MainPage.ANSWER_3),
                                         (MainPage.QUESTION_4, MainPage.ANSWER_4),
                                         (MainPage.QUESTION_5, MainPage.ANSWER_5),
                                         (MainPage.QUESTION_6, MainPage.ANSWER_6),
                                         (MainPage.QUESTION_7, MainPage.ANSWER_7),
                                         (MainPage.QUESTION_8, MainPage.ANSWER_8)])
    def test_faq_questions(self, n, expected):
        self.driver.get(Urls.URL_MAIN)

        main_page = MainPage(self.driver)
        MainPage.wait_for_load_home_page(self)
        read_answer = MainPage.get_answer(n)

        assert read_answer == expected

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()