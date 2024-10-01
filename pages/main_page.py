from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure

class MainPage(BasePage):

    @allure.step('Клик по логотипу Самокат')
    def click_logo_scooter(self):
        self.find_element_located_click(MainPageLocators.LOGO)

    @allure.step('Клик по логотипу Яндекс')
    def click_logo_yandex(self):
        self.find_element_located_click(MainPageLocators.YANDEX_BUTTON)
    #Принять куки
    def check_cookie(self):
        cookie = self.find_element_located(MainPageLocators.COOKIE_MESSAGE)
        if cookie:
            cookie.click()
        else:
            pass

    @allure.step('Возвращаем значение ответа от требуемого вопроса')
        # метод кликает по Вопросу
    def main_page_faq(self, question, answer):
        self.check_cookie()
        search_field = self.find_element_located(question)
        self.execute_script(search_field)
        self.find_element_to_be_clickable(question)
        search_field.click()
        # метод ищет ответ в раскрытой вкладке
        return self.find_element_located(answer).text

    @allure.step('Определение местоположения на Дзен странице')
    def find_dzen_logo(self):
        self.find_element_located(MainPageLocators.DZEN_PAGE)





