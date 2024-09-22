from urls_credits import Urls
import pytest
from selenium import webdriver
from main_page import MainPage
from order_page import OrderPage

class TestOrder1:

    driver = None

    @classmethod
    def setup_class(cls):
  #       создали драйвер для браузера
        cls.driver = webdriver.Firefox()


    @pytest.mark.parametrize("name, surname, address, station, phone, data, days, color", [
        ("Иван", "Иванов", "Москва, ул. Ленина, 1", "Академическая", "88005553535", "1.10.2024", "двое суток", "чёрный жемчуг" ),
        ("Петр", "Петров", "Санкт-Петербург, пр. Невский, 1", "Академическая", "88005553535", "1.10.2024", "двое суток", "чёрный жемчуг")
    ])
    def test_order_flow(self, name, surname, address, station, phone, data, days, color):
        self.driver.get(URL_MAIN)
        main_page = MainPage(self, driver)
        main_page.click_order_up_button()
        order_page.fill_order_form_1(name, surname, address, station, phone)
        order_page.click_order_form_1()
        order_page.fill_order_form_2(data, days, color)
        order_page.click_order_form_2()


        assert "Заказ успешно создан" in order_page.get_success_message()  # Проверьте текст сообщения

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

class TestOrder2:

    driver = None

    @classmethod
    def setup_class(cls):
  #       создали драйвер для браузера
        cls.driver = webdriver.Firefox()


    @pytest.mark.parametrize("name, surname, address, station, phone, data, days, color", [
        ("Иван", "Иванов", "Москва, ул. Ленина, 1", "Академическая", "88005553535", "1.10.2024", "двое суток", "чёрный жемчуг" ),
        ("Петр", "Петров", "Санкт-Петербург, пр. Невский, 1", "Академическая", "88005553535", "1.10.2024", "двое суток", "чёрный жемчуг")
    ])
    def test_order_flow(self, name, surname, address, station, phone, data, days, color):
        self.driver.get(URL_MAIN)
        main_page = MainPage(self, driver)
        main_page.click_order_middle_button()
        order_page.fill_order_form_1(name, surname, address, station, phone)
        order_page.click_order_form_1()
        order_page.fill_order_form_2(data, days, color)
        order_page.click_order_form_2()


        assert "Заказ успешно создан" in order_page.get_success_message()  # Проверьте текст сообщения

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()