from pages.login_page import LoginPage

VALID_EMAIL = "testdima@gmail.com"
VALID_PASSWORD = "Test@123456"
INVALID_EMAIL = "testdima@gmail"
INVALID_PASSWORD = "Test1"

def test_login_success(driver):

    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.click_login_btn()

    assert login_page.is_logged() is True

def test_login_wrong_email(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(INVALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.click_login_btn()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()

def test_login_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(INVALID_PASSWORD)
    login_page.click_login_btn()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()

def test_login_unregistered(driver):

    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email("yakub@1345.com")
    login_page.fill_password("Test@123456")
    login_page.click_login_btn()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()