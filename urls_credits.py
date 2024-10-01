from locators.main_page_locators import MainPageLocators
class Urls:

    BASE_URL = "https://qa-scooter.praktikum-services.ru/"
    ORDER_URL = "https://qa-scooter.praktikum-services.ru/order"
    DZEN_URL = "https://dzen.ru/?yredirect=true"

class Messages:
    MESSAGE = "Заказ оформлен"

class Order:
    Users = [["Иван", "Иванов", "Москва, ул. Ленина, 1", "Черкизовская", "88005553535", "1.10.2024", "Оплата наличными", Messages.MESSAGE],
             ["Анна", "Петрова", "Питер, ул. Пушкина, 10", "ВДНХ", "88001001010", "10.11.2024", "В домофон не звонить!", Messages.MESSAGE]]





class Answers:
    ANSWER_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ANSWER_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    ANSWER_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    ANSWER_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    ANSWER_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    ANSWER_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    ANSWER_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    ANSWER_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

class Testdata:
    test_data = [[MainPageLocators.QUESTION_1, MainPageLocators.TEXT_1, Answers.ANSWER_1],
                 [MainPageLocators.QUESTION_2, MainPageLocators.TEXT_2, Answers.ANSWER_2],
                 [MainPageLocators.QUESTION_3, MainPageLocators.TEXT_3, Answers.ANSWER_3],
                 [MainPageLocators.QUESTION_4, MainPageLocators.TEXT_4, Answers.ANSWER_4],
                 [MainPageLocators.QUESTION_5, MainPageLocators.TEXT_5, Answers.ANSWER_5],
                 [MainPageLocators.QUESTION_6, MainPageLocators.TEXT_6, Answers.ANSWER_6],
                 [MainPageLocators.QUESTION_7, MainPageLocators.TEXT_7, Answers.ANSWER_7],
                 [MainPageLocators.QUESTION_8, MainPageLocators.TEXT_8, Answers.ANSWER_8]]

