from base_page import BasePage
from locators import Locators
import allure

class MainPage(BasePage):

    @allure.step('Открываем страницу оформления заказа нажатием на кнопку Заказать')  # декоратор
    def click_on_the_order_button(self, locator):
        return self.find_element(locator, time=10).click()


    # метод кликает по Вопросу
    @allure.step('Клик по вопросу для раскрытия поля Ответ')
    def click_question(self, locator_question):
        return self.find_element(locator_question, time=10).click()

    # метод ищет ответ в раскрытой вкладке
    @allure.step('Ищем ответ в раскрытой вкладке')
    def check_answer(self, locator_answer):
         return self.find_element(locator_answer).text





