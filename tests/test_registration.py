import time

from faker import Faker

from pages.registration_page import RegistrationPage

fake = Faker()

VALID_PASSWORD = "Test@12345"
VALID_EMAIL = fake.email()
REGISTERED_EMAIL = "testdima@gmail.com"
INVALID_EMAIL = "testdima@gmail."
INVALID_PASSWORD = "Test1"


def test_registration_success(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email_and_password(VALID_EMAIL, VALID_PASSWORD)
    time.sleep(2)
    registration_page.click_registration_btn()
    assert registration_page.is_logged() is True

def test_registration_already_registered(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email_and_password(REGISTERED_EMAIL, VALID_PASSWORD)
    time.sleep(2)
    registration_page.click_registration_btn()
    assert registration_page.get_alert_text() == "User already exist"
    registration_page.accept_alert()

def test_registration_invalid_email(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email_and_password(INVALID_EMAIL, VALID_PASSWORD)
    time.sleep(2)
    registration_page.click_registration_btn()
    assert registration_page.get_alert_text() == ('Wrong email or password format\n'
 '            Email must contains one @ and minimum 2 symbols after last dot\n'
 '            Password must contain at least one uppercase letter!\n'
 '            Password must contain at least one lowercase letter!\n'
 '            Password must contain at least one digit!\n'
 '            Password must contain at least one special symbol from '
 '[‘$’,’~’,’-‘,’_’]!')
    registration_page.accept_alert()
#
# def test_registration_invalid_password(driver):
#     registration_page = RegistrationPage(driver)
#     registration_page.open_registration_form()
#     registration_page.fill_email_and_password(VALID_EMAIL, INVALID_PASSWORD)
#     time.sleep(2)
#     registration_page.click_registration_btn()
#     assert registration_page.get_alert_text() == ('Wrong email or password format\n'
#  '            Email must contains one @ and minimum 2 symbols after last dot\n'
#  '            Password must contain at least one uppercase letter!\n'
#  '            Password must contain at least one lowercase letter!\n'
#  '            Password must contain at least one digit!\n'
#  '            Password must contain at least one special symbol from '
#  '[‘$’,’~’,’-‘,’_’]!')
#     registration_page.accept_alert()

def test_registration_invalid_password(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_form()
    registration_page.fill_email_and_password(VALID_EMAIL, INVALID_PASSWORD)

    registration_page.click_registration_btn()
    alert_text = registration_page.get_alert_text()
    assert 'Wrong email or password format' in alert_text
    registration_page.accept_alert()


