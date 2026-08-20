import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://telranedu.web.app/')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

