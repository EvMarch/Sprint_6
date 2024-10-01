import pytest
from selenium import webdriver
from urls_credits import Urls

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.get(Urls.BASE_URL)
    yield driver
    driver.quit()