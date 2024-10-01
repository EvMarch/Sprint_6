import allure
from pages.main_page import MainPage
from urls_credits import Urls

class TestLogoYandex:
    @allure.title('Переход в dzen, через логотип Яндекс')
    def test_jump_after_click_logo_yandex(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site(Urls.BASE_URL)
        main_page.click_logo_yandex()
        main_page.switch_window()
        main_page.find_dzen_logo()
        url = main_page.current_url()
        assert Urls.DZEN_URL in url