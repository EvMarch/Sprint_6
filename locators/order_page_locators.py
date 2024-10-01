from selenium.webdriver.common.by import By

class OrderPageLocators:
    # локатор кнопки «Заказать» в шапке страницы
    ORDER_UP_BUTTON = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']"]

    # локатор кнопки «Заказать» в середине страницы
    ORDER_DOWN_BUTTON = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text() = 'Заказать']"]



    #Поля заполнения страницы заказа 1
    SUCCESS_MESSAGE = [By.CLASS_NAME, "Order_Notice"]
    NAME_FIELD = [By.XPATH, "//input[@placeholder='* Имя']"]
    SURNAME_FIELD = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS_FIELD = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    STATION_FIELD = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    PHONE_FIELD = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Далее']"]
    # Поля заполнения страницы заказа 2
    DATA_FIELD= [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]
    DAYS_FIELD = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    DAYS_COUNTER = [By.XPATH, ".//div[text()='сутки']"]
    COLOR_FIELD = [By.ID, "black"]
    COMMENT_FIELD = [By.XPATH, "//input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"]
    ORDER_BUTTON = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Заказать']"]
    YES_BUTTON = [By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Да']"]
    ORDER_INFO = [By.XPATH, ".//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']"]