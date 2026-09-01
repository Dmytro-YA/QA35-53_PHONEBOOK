import pytest
from selenium import webdriver

from data.user_data import exiting_user
from pages.login_page import LoginPage



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://telranedu.web.app/')
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def authenticated_driver(driver):
    login_page = LoginPage(driver)
    user = exiting_user()
    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.click_login_btn()
    return driver
