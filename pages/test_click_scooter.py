import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from urls_credits import Urls

class TestLogoScooter:

    @allure.title('Переход на главную, через логотип Самокат (из меню Заказать в шапке)')
    def test_go_click_logo_scooter_in_header(self, browser):
        main_page = MainPage(browser)
        order_button = OrderPage(browser)
        main_page.go_to_site(Urls.BASE_URL)
        order_button.order_for_header()
        main_page.click_logo_scooter()
        url = main_page.current_url()
        assert url == Urls.BASE_URL

    @allure.title('Переход на главную, через логотип Самокат (из меню Заказать в футере)')
    def test_go_click_logo_scooter_in_footer(self, browser):
        main_page = MainPage(browser)
        order_button = OrderPage(browser)
        main_page.go_to_site(Urls.BASE_URL)
        order_button.order_for_footer()
        main_page.click_logo_scooter()
        url = main_page.current_url()
        assert url == Urls.BASE_URL