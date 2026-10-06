import logging

from data.user_data import create_user, exiting_user, invalid_email_user, invalid_password_user
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)

def test_login_success(driver):
    logger.info("Starting test_login_success")
    login_page = LoginPage(driver)
    user = exiting_user()
    logger.info(f"Logging in as {user.username}")
    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.click_login_btn()

    assert login_page.is_logged() is True

def test_login_wrong_email(driver):
    logger.info(f"Starting test_login_wrong_email with user: {invalid_email_user().username}")
    login_page = LoginPage(driver)
    user = invalid_email_user()

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.click_login_btn()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()

def test_login_wrong_password(driver):
    logger.info(f"Starting test_login_wrong_password with user: {invalid_password_user().username}")
    login_page = LoginPage(driver)
    user = invalid_password_user()

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.click_login_btn()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()

def test_login_unregistered(driver):
    logger.info("Starting test_login_unregistered")
    login_page = LoginPage(driver)
    user = create_user(username="dssdsd@gnmail.com", password="QWEwer123!")

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.click_login_btn()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()