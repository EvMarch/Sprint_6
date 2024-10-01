from selenium.webdriver.common.by import By

class MainPageLocators:
    # Вопросы
    QUESTION_1 = [By.ID, "accordion__heading-0"]
    QUESTION_2 = [By.ID, "accordion__heading-1"]
    QUESTION_3 = [By.ID, "accordion__heading-2"]
    QUESTION_4 = [By.ID, "accordion__heading-3"]
    QUESTION_5 = [By.ID, "accordion__heading-4"]
    QUESTION_6 = [By.ID, "accordion__heading-5"]
    QUESTION_7 = [By.ID, "accordion__heading-6"]
    QUESTION_8 = [By.ID, "accordion__heading-7"]

    # Предполагаемый текст ответов
    TEXT_1 = [By.ID, "accordion__panel-0"]
    TEXT_2 = [By.ID, "accordion__panel-1"]
    TEXT_3 = [By.ID, "accordion__panel-2"]
    TEXT_4 = [By.ID, "accordion__panel-3"]
    TEXT_5 = [By.ID, "accordion__panel-4"]
    TEXT_6 = [By.ID, "accordion__panel-5"]
    TEXT_7 = [By.ID, "accordion__panel-6"]
    TEXT_8 = [By.ID, "accordion__panel-7"]

    # локатор поля «Яндекс» в шапке страницы
    YANDEX_BUTTON = [By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']"]
    COOKIE_MESSAGE = (By.ID, 'rcc-confirm-button')
    DZEN_PAGE = (By.ID, "__SVG_SPRITE_NODE__")

    # логотип Самокат
    LOGO = [By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']"]