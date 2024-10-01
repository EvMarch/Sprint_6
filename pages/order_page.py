from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
import allure

class OrderPage(BasePage):

    @allure.step('Клик на кнопку Заказать в шапке стенда')
    def order_for_header(self):
        self.find_element_located_click(OrderPageLocators.ORDER_UP_BUTTON)

    @allure.step('Открытие формы заказа, через кнопку "Заказ" в футере')
    def order_for_footer(self):
        self.scroll_page()
        self.find_element_located_click(OrderPageLocators.ORDER_DOWN_BUTTON)

    @allure.step('Оформление заказа по заданным учеткам пользователей')
    def order_form(self, first_name, last_name, address, station, phone, date, comment):
        self.find_element_located(OrderPageLocators.NAME_FIELD).send_keys(first_name)
        self.find_element_located(OrderPageLocators.SURNAME_FIELD).send_keys(last_name)
        self.find_element_located(OrderPageLocators.ADDRESS_FIELD).send_keys(address)
        self.find_element_located_click(OrderPageLocators.STATION_FIELD)
        self.find_element_located(OrderPageLocators.STATION_FIELD).send_keys(station)
        self.find_element_located(OrderPageLocators.STATION_FIELD).send_keys(Keys.ARROW_UP)
        self.find_element_located(OrderPageLocators.STATION_FIELD).send_keys(Keys.ENTER)
        self.find_element_located(OrderPageLocators.PHONE_FIELD).send_keys(phone)
        self.find_element_located_click(OrderPageLocators.NEXT_BUTTON)
        self.find_element_located(OrderPageLocators.DATA_FIELD).send_keys(date)
        self.find_element_located_click(OrderPageLocators.DAYS_FIELD)
        self.find_element_located_click(OrderPageLocators.DAYS_COUNTER)
        self.find_element_located_click(OrderPageLocators.COLOR_FIELD)
        self.find_element_located(OrderPageLocators.COMMENT_FIELD).send_keys(comment)
        self.find_element_located_click(OrderPageLocators.ORDER_BUTTON)
        self.find_element_located_click(OrderPageLocators.YES_BUTTON)
        order_complete = self.find_element_located(OrderPageLocators.ORDER_INFO)
        return order_complete.text


