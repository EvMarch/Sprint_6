from selenium.webdriver.common.by import By

class Locators:
    # локатор кнопки «Заказать» в шапке страницы
    ORDER_UP_BUTTON = [By.XPATH, ".//div/div[1]/div[2]/button[1]"]

    # локатор кнопки «Заказать» в середине страницы
    ORDER_MIDDLE_BUTTON = [By.XPATH, ".//div/div/div[1]/div[4]/div[2]/div[5]/button"]

    STATUS_BUTTON = [By.XPATH, ".//html/body/div/div/div[2]/div[5]/div[2]/button"]

    # локатор поля «Яндекс» в шапке страницы
    YANDEX_BUTTON = [By.XPATH, ".//div/div[1]/div[1]/a[1]"]

    # логотип Самокат
    LOGO = [By.XPATH, ".//div/div[1]/div[1]/a[2]"]

    #Вопросы
    QUESTION_1 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[1]/div[1]/div"]
 #   / html / body / div[1] / div / div / div[5] / div[2] / div / div[1] / div[1]
  #  / html / body / div[1] / div / div / div[5] / div[2] / div / div[2] / div[1]

    #// *[ @ id = "accordion__heading-0"]
    #// *[ @ id = "accordion__heading-1"]
   # / html / body / div[1] / div / div / div[5] / div[2] / div / div[2] / div[1] / div
   # QUESTION_2 = (By.ID,"accordion__heading-1")
    QUESTION_2 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[2]/div[1]/div"]
    QUESTION_3 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[3]/div[1]/div"]

    QUESTION_4 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[4]/div[1]/div"]
    QUESTION_5 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[5]/div[1]/div"]
    QUESTION_6 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[6]/div[1]/div"]
    QUESTION_7 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[7]/div[1]/div"]
    QUESTION_8 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[8]/div[1]/div"]
  #  / html / body / div[1] / div / div / div[5] / div[2] / div / div[8] / div[1] / div
   # / html / body / div[1] / div / div / div[5] / div[2] / div / div[7] / div[1] / div
   # / html / body / div[1] / div / div / div[5] / div[2] / div / div[7] / div[2] / p

    #Предполагаемый текст ответов
    TEXT_1 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[1]/div[2]/p"]
    TEXT_2 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[2]/div[2]/p"]
    TEXT_3 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[3]/div[2]/p"]
    TEXT_4 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[4]/div[2]/p"]
    TEXT_5 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[5]/div[2]/p"]
    TEXT_6 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[6]/div[2]/p"]
    TEXT_7 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[7]/div[2]/p"]
    TEXT_8 = [By.XPATH,".//div[1]/div/div/div[5]/div[2]/div/div[8]/div[2]/p"]
    #TEXT_8 = (By.ID,"accordion__heading-7")

    #/ html / body / div[1] / div / div / div[5] / div[2] / div / div[1] / div[2]
   # / html / body / div[1] / div / div / div[5] / div[2] / div / div[8] / div[2]

    #Поля заполнения страницы заказа 1
    SUCCESS_MESSAGE = [By.CLASS_NAME, "Order_Notice"]
    NAME_FIELD = [By.XPATH, "//div/div[2]/div[2]/div[1]/input"]
    SURNAME_FIELD = [By.XPATH, "//div/div[2]/div[2]/div[2]/input"]
    ADDRESS_FIELD = [By.XPATH, "//div/div[2]/div[2]/div[3]/input"]
    STATION_FIELD = [By.XPATH, "//div/div[2]/div[2]/div[4]/div/div[1]"]
    STATION_NAME = [By.XPATH, "//div/div[2]/div[2]/div[4]/div/div[2]/ul/li[1]/button"]
    PHONE_FIELD = [By.XPATH, "//div/div[2]/div[2]/div[5]/input"]
    NEXT_BUTTON = [By.XPATH, "//div/div[2]/div[3]/button"]
    # Поля заполнения страницы заказа 2
    DATA_FIELD= [By.XPATH, "//div/div[2]/div[2]/div[1]/div[1]/div/input"]
    DAYS_FIELD = [By.XPATH, "//div/div[2]/div[2]/div[2]/div/div[2]/span"]
    DAYS_COUNTER = [By.XPATH, "//div/div[2]/div[2]/div[2]/div[2]/div[1]"]
    COLOR_FIELD = [By.XPATH, "//div/div[2]/div[2]/div[3]/label[1]/input"]
    ORDER_BUTTON = [By.XPATH, "//div/div[2]/div[3]/button[2]"]
    YES_BUTTON = [By.XPATH, "//div/div/div[2]/div[5]/div[2]/button[2]"]