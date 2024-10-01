from urls_credits import Urls, Order
from pages.order_page import OrderPage
from pages.main_page import MainPage
import pytest
import allure

class TestOrderForHeader:
    @allure.title("Оформление заказа через кнопку Заказать в шапке")
    @pytest.mark.parametrize('name, surname, address, station, phone, date, comment, expected_result', Order.Users)
    def test_order_page_for_header(self, browser, name, surname, address, station, phone, date, comment,
                                   expected_result):
        page = OrderPage(browser)
        main_page = MainPage(browser)
        main_page.go_to_site(Urls.BASE_URL)
        page.order_for_header()
        order_for_header_button_complete = page.order_form(name, surname, address, station, phone, date, comment)
        assert expected_result in order_for_header_button_complete

    @allure.description('Тест успешного создания заказа при переходе на страницу заказа по кнопке внизу страницы')
    @pytest.mark.parametrize('name, surname, address, station, phone, date, comment, expected_result', Order.Users)
    def test_order_page_for_footer(self, browser, name, surname, address, station, phone, date, comment,
                                   expected_result):
        page = OrderPage(browser)
        main_page = MainPage(browser)
        main_page.go_to_site(Urls.BASE_URL)
        main_page.check_cookie()
        page.order_for_footer()
        order_for_footer_button_complete = page.order_form(name, surname, address, station, phone, date, comment)
        assert expected_result in order_for_footer_button_complete
