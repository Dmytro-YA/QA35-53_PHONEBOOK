import pytest
from selenium import webdriver

from data.contact_data import create_contact
from data.user_data import exiting_user
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage
from pages.login_page import LoginPage
import logging

from utils.logger_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    logger.info("Starting browser session")
    driver = webdriver.Chrome()
    driver.get('https://telranedu.web.app/')
    driver.implicitly_wait(5)

    yield driver
    logger.info("Closing browser session")
    driver.quit()


@pytest.fixture
def authenticated_driver(driver):
    login_page = LoginPage(driver)
    user = exiting_user()
    logger.info(f"Logging in as {user.username}")
    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.click_login_btn()
    return driver

@pytest.fixture
def ensure_min_contacts(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contacts_page.open_contacts_link()
    count = contacts_page.total_contacts_count()
    if count< 3:
        logger.warning(f"There are only {count} contacts, adding more")

    while contacts_page.total_contacts_count() < 3:
        contact_page.create_contact_steps(create_contact())
        contacts_page.open_contacts_link()
    return authenticated_driver
