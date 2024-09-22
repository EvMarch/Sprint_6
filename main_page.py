from selenium.webdriver.common.by import By
from urls_credits import Urls
import pytest

class MainPage:
    # локатор поля «Заказать» в шапке страницы
    ORDER_UP_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g']
    # локатор поля «Заказать» в середине страницы
    ORDER_MIDDLE_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM']
    # вопросы в раскрывающемся списке


    QUESTION_1 = [By.ID, "accordion__heading-0"]
    QUESTION_2 = [By.ID, "accordion__heading-1"]
    QUESTION_3 = [By.ID, "accordion__heading-2"]
    QUESTION_4 = [By.ID, "accordion__heading-3"]
    QUESTION_5 = [By.ID, "accordion__heading-4"]
    QUESTION_6 = [By.ID, "accordion__heading-5"]
    QUESTION_7 = [By.ID, "accordion__heading-6"]
    QUESTION_8 = [By.ID, "accordion__heading-7"]


    ANSWER_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ANSWER_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    ANSWER_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    ANSWER_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    ANSWER_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    ANSWER_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    ANSWER_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    ANSWER_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.profile_description))

    # метод кликает по Вопросу
    def open_question(self, question):
        self.driver.find_element(question).click()

    # метод ищет ответ в раскрытой вкладке

    def get_answer(self, answer):
        return self.driver.find_element(answer).text

    # метод кликает на кнопку Заказать в шапке страницы

    def new_order(self, order):
        self.driver.find_element(order).click()


