import logging
import pytest
from data.user_data import create_user
from pages.registration_page import RegistrationPage

logger = logging.getLogger(__name__)

@pytest.mark.smoke
@pytest.mark.parametrize("u", [create_user()])
def test_reg_obj_success(driver, u):
    logger.info(f"Starting test_reg_obj_success for user: {u.username}")
    rp = RegistrationPage(driver)
    rp.open_registration_form()
    rp.fill_email_and_password(u.username, u.password)
    rp.click_registration_btn()
    assert rp.is_logged()

@pytest.mark.regression
@pytest.mark.parametrize("u", [
    create_user(username="dmitrigmail.com"),
    create_user(password="Test12345")
])
def test_reg_obj_neg(driver, u):
    logger.info(f"Starting test_reg_obj_neg for user: {u.username}")
    rp = RegistrationPage(driver)
    rp.open_registration_form()
    rp.fill_email_and_password(u.username, u.password)
    rp.click_registration_btn()
    assert 'Wrong email or password format' in rp.get_alert_text()
    rp.accept_alert()
