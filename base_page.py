from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл страницы до конца сниз')
    def scroll_page(self):
        return self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step('Скролл страницы вниз')
    def scroll_page_down(self):
        return self.driver.execute_script("window.scrollBy(0, 2000)")

    @allure.step('Поиск элемента на странице')
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    @allure.step('Ожидание прогрузки элемента на странице')
    def wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Открываем страницу')
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step('Переключение на другое окно браузера')
    def switch_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание подгрузки окна')
    def window_wait(self, expected_url):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

