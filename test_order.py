from urls_credits import Urls, Order
from locators import Locators
from main_page import MainPage
from order_page import OrderPage
import pytest
import allure

@allure.description('Тест успешного создания заказа при переходе на страницу заказа по кнопке вверху страницы')
@pytest.mark.parametrize('name, surname, address, phone, date', Order.Users)
def test_order_up_button(browser, name, surname, address, phone, date):
    yandex_page = MainPage(browser)
    order_page = OrderPage(browser)
    yandex_page.go_to_site(Urls.BASE_URL)
    yandex_page.click_on_the_order_button(Locators.ORDER_UP_BUTTON)
    order_page.wait(Locators.NAME_FIELD)
    order_page.fill_field(Locators.NAME_FIELD, name)
    order_page.fill_field(Locators.SURNAME_FIELD, surname)
    order_page.fill_field(Locators.ADDRESS_FIELD, address)
    order_page.click_button(Locators.STATION_FIELD)
    order_page.click_button(Locators.STATION_NAME)
    order_page.fill_field(Locators.PHONE_FIELD, phone)
    order_page.click_button(Locators.NEXT_BUTTON)
    order_page.click_button(Locators.DATA_FIELD)
    order_page.fill_field(Locators.DATA_FIELD, date)
    order_page.click_button(Locators.DAYS_FIELD)
    order_page.click_button(Locators.DAYS_COUNTER)
    order_page.click_button(Locators.COLOR_FIELD)
    order_page.click_button(Locators.ORDER_BUTTON)
    order_page.click_button(Locators.YES_BUTTON)
    assert "Заказ оформлен" in browser.page_source  # Проверьте текст сообщения

@allure.description('Тест успешного создания заказа при переходе на страницу заказа по кнопке внизу страницы')
@pytest.mark.parametrize('name, surname, address, phone, date', Order.Users)
def test_order_middle_button(browser, name, surname, address, phone, date):
    yandex_page = MainPage(browser)
    order_page = OrderPage(browser)
    yandex_page.go_to_site(Urls.BASE_URL)
    yandex_page.scroll_page_down()
    yandex_page.click_on_the_order_button(Locators.ORDER_MIDDLE_BUTTON)
    order_page.wait(Locators.NAME_FIELD)
    order_page.fill_field(Locators.NAME_FIELD, name)
    order_page.fill_field(Locators.SURNAME_FIELD, surname)
    order_page.fill_field(Locators.ADDRESS_FIELD, address)
    order_page.click_button(Locators.STATION_FIELD)
    order_page.click_button(Locators.STATION_NAME)
    order_page.fill_field(Locators.PHONE_FIELD, phone)
    order_page.click_button(Locators.NEXT_BUTTON)
    order_page.click_button(Locators.DATA_FIELD)
    order_page.fill_field(Locators.DATA_FIELD, date)
    order_page.click_button(Locators.DAYS_FIELD)
    order_page.click_button(Locators.DAYS_COUNTER)
    order_page.click_button(Locators.COLOR_FIELD)
    order_page.click_button(Locators.ORDER_BUTTON)
    order_page.click_button(Locators.YES_BUTTON)
    assert "Заказ оформлен" in browser.page_source  # Проверьте текст сообщения

@allure.description('Тест успешного перехода на главную страницу Яндекс.Самокат')
def test_click_logo(browser):
    order_page = OrderPage(browser)
    order_page.go_to_site(Urls.ORDER_URL)
    order_page.click_button(Locators.LOGO)
    assert "Самокат " in browser.page_source

@allure.description('Тест перехода на страницу Яндекс.Дзен')
def test_click_yandex(browser):
    order_page = OrderPage(browser)
    order_page.go_to_site(Urls.ORDER_URL)
    order_page.click_button(Locators.YANDEX_BUTTON)
    order_page.switch_window()
    order_page.window_wait(Urls.DZEN_URL)
    assert browser.current_url == Urls.DZEN_URL