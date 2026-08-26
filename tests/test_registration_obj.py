import uuid

from models.user import User
from pages.registration_page import RegistrationPage


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)

    random_suffix = uuid.uuid4().hex[:8]

    user = User(
        f"dmitri{random_suffix}@gmail.com",
        "Test12345@"
    )
    registration_page.open_registration_form()
    registration_page.fill_email_and_password(user.username,user.password)
    registration_page.click_registration_btn()

    assert registration_page.is_logged() is True


def test_registration_wrong_email(driver):
    registration_page = RegistrationPage(driver)



    user = User(
        "dmitrigmail.com",
        "Test12345@"
    )
    registration_page.open_registration_form()
    registration_page.fill_email_and_password(user.username, user.password)
    registration_page.click_registration_btn()

    alert_text = registration_page.get_alert_text()
    assert 'Wrong email or password format' in alert_text
    registration_page.accept_alert()


def test_registration_wrong_password(driver):
    registration_page = RegistrationPage(driver)

    user = User(
        "dmitri@gmail.com",
        "Test12345"
    )
    registration_page.open_registration_form()
    registration_page.fill_email_and_password(user.username, user.password)
    registration_page.click_registration_btn()

    alert_text = registration_page.get_alert_text()
    assert 'Wrong email or password format' in alert_text
    registration_page.accept_alert()
