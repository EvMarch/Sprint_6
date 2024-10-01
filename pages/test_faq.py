from urls_credits import Urls, Testdata
from pages.main_page import MainPage
import allure
import pytest

class TestFaq:

    @allure.title('Тест раскрытия вопроса и проверка соответствующего текста ответа')
    @pytest.mark.parametrize('button, answer, expected_result', Testdata.test_data)
    def test_faq_questions(self, button, answer, expected_result, browser):
        yandex_main_page = MainPage(browser)
        yandex_main_page.go_to_site(Urls.BASE_URL)
        get_answer = yandex_main_page.main_page_faq(button, answer)
        assert get_answer == expected_result





