from selenium.webdriver.common.by import By
from main_page import MainPage
from urls_credits import Urls

class OrderPage(MainPage):
    SUCCESS_MESSAGE = [By.CLASS_NAME, "Order_Notice"]
    NAME_FIELD = [By.XPATH, "//p[text() = '* Имя'"]
    SURNAME_FIELD = [By.XPATH, "//p[text() = '* Фамилия'"]
    ADDRESS_FIELD = [By.XPATH, "//p[text() = '* Адрес: куда привезти заказ'"]
    STATION_FIELD = [By.XPATH, "//p[text() = '* Станция метро'"]
    PHONE_FIELD = [By.XPATH, "//p[text() = '* Телефон: на него позвонит курьер'"]
    NEXT_BUTTON = [By.XPATH, "//p[text() = 'Далее'"]
    DATA_FIELD= [By.XPATH, "//p[text() = '* Когда привезти самокат'"]
    DAYS_FIELD = [By.XPATH, "//p[text() = '* Срок аренды'"]
    COLOR_FIELD = [By.XPATH, "//p[text() = '* Чёрный жемчуг'"]
    ORDER_BUTTON = [By.XPATH, "//p[text() = 'Заказать'"]

    def __init__(self, driver):
        self.driver = driver

    def click_order_up_button(self):
        self.driver.find_element(MainPage.ORDER_UP_BUTTON).click()

    def click_order_middle_button(self):
        self.driver.find_element(MainPage.ORDER_MIDDLE_BUTTON).click()



    def fill_order_form_1(self, name, surname, address, station, phone):
        # Заполнение формы. Пример:
        self.driver.find_element(NAME_FIELD).send_keys(name)
        self.driver.find_element(SURNAME_FIELD).send_keys(surname)
        self.driver.find_element(ADDRESS_FIELD).send_keys(address)
        self.driver.find_element(STATION_FIELD).send_keys(station)
        self.driver.find_element(PHONE_FIELD).send_keys(phone)

    def click_order_form_1(self):

        self.driver.click_order_form_1(NEXT_BUTTON).click()


    def fill_order_form_2(self, data, days, color):
        self.driver.find_element(DATA_FIELD).send_keys(data)
        self.driver.find_element(DAYS_FIELD).send_keys(days)
        self.driver.find_element(COLOR_FIELD).send_keys(color)
        self.driver.find_element(ORDER_BUTTON).click()

    def click_order_form_2(self):
        self.driver.find_element(ORDER_BUTTON).click()

    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text