from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def go_to_site(self, url):
        return self.browser.get(url)

    def current_url(self):
        return self.browser.current_url

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_element_located_click(self, locator):
        self.find_element_located(locator).click()

    def find_element_to_be_clickable(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Can't find element by locator {locator}")

    def execute_script(self, locator):
        return self.browser.execute_script("arguments[0].scrollIntoView();", locator)


    def switch_window(self):
        return self.browser.switch_to.window(self.browser.window_handles[-1])

    def scroll_page(self):
        return self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")


