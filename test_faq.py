from locators import Locators
from urls_credits import Urls, Answers
from main_page import MainPage
import allure

@allure.description('Тест раскрытия вопроса 1 и текст ответа соответствующий')
def test_faq_questions(browser):
    yandex_main_page = MainPage(browser)
    yandex_main_page.go_to_site(Urls.BASE_URL)
    yandex_main_page.scroll_page()
    yandex_main_page.click_question(Locators.QUESTION_1)
    yandex_main_page.wait(Locators.TEXT_1)
    assert Answers.ANSWER_1 in browser.page_source

@allure.description('Тест раскрытия вопроса 2 и текст ответа соответствующий')
def test_faq_questions(browser):
    yandex_main_page = MainPage(browser)
    yandex_main_page.go_to_site(Urls.BASE_URL)
    yandex_main_page.scroll_page()
    yandex_main_page.click_question(Locators.QUESTION_2)
    yandex_main_page.wait(Locators.TEXT_2)
    assert Answers.ANSWER_2 in browser.page_source

@allure.description('Тест раскрытия вопроса 3 и текст ответа соответствующий')
def test_faq_questions(browser):
    yandex_main_page = MainPage(browser)
    yandex_main_page.go_to_site(Urls.BASE_URL)
    yandex_main_page.scroll_page()
    yandex_main_page.click_question(Locators.QUESTION_3)
    yandex_main_page.wait(Locators.TEXT_3)
    assert Answers.ANSWER_3 in browser.page_source

@allure.description('Тест раскрытия вопроса 4 и текст ответа соответствующий')
def test_faq_questions(browser):
    yandex_main_page = MainPage(browser)
    yandex_main_page.go_to_site(Urls.BASE_URL)
    yandex_main_page.scroll_page()
    yandex_main_page.click_question(Locators.QUESTION_4)
    yandex_main_page.wait(Locators.TEXT_4)
    assert Answers.ANSWER_4 in browser.page_source

@allure.description('Тест раскрытия вопроса 5 и текст ответа соответствующий')
def test_faq_questions(browser):
    yandex_main_page = MainPage(browser)
    yandex_main_page.go_to_site(Urls.BASE_URL)
    yandex_main_page.scroll_page()
    yandex_main_page.click_question(Locators.QUESTION_5)
    yandex_main_page.wait(Locators.TEXT_5)
    assert Answers.ANSWER_5 in browser.page_source

@allure.description('Тест раскрытия вопроса 6 и текст ответа соответствующий')
def test_faq_questions(browser):
    yandex_main_page = MainPage(browser)
    yandex_main_page.go_to_site(Urls.BASE_URL)
    yandex_main_page.scroll_page()
    yandex_main_page.click_question(Locators.QUESTION_6)
    yandex_main_page.wait(Locators.TEXT_6)
    assert Answers.ANSWER_6 in browser.page_source

@allure.description('Тест раскрытия вопроса 7 и текст ответа соответствующий')
def test_faq_questions(browser):
    yandex_main_page = MainPage(browser)
    yandex_main_page.go_to_site(Urls.BASE_URL)
    yandex_main_page.scroll_page()
    yandex_main_page.click_question(Locators.QUESTION_7)
    yandex_main_page.wait(Locators.TEXT_7)
    assert Answers.ANSWER_7 in browser.page_source

@allure.description('Тест раскрытия вопроса 8 и текст ответа соответствующий')
def test_faq_questions(browser):
    yandex_main_page = MainPage(browser)
    yandex_main_page.go_to_site(Urls.BASE_URL)
    yandex_main_page.scroll_page()
    yandex_main_page.click_question(Locators.QUESTION_8)
    yandex_main_page.wait(Locators.TEXT_8)
    assert Answers.ANSWER_8 in browser.page_source


