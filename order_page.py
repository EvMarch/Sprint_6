from base_page import BasePage
from locators import Locators
import allure

class OrderPage(BasePage):

    @allure.step('заполнение поля ввода ')
    def fill_field(self, locator, text):
     self.find_element(locator).send_keys(text)



    @allure.step('Клик на кнопку')
    def click_button(self, locator):
        self.find_element(locator).click()

    @allure.step('Клик на кнопку Заказать')
    def click_order_form_2(self):
        self.driver.find_element(Locators.ORDER_BUTTON).click()

    @allure.step('Клик на кнопку Да в окне Хотите оформить заказ?')
    def click_yes(self):
        self.driver.find_element(Locators.YES_BUTTON).click()

