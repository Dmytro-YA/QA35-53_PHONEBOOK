import logging
import pytest
from data.contact_data import create_contact
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage

logger = logging.getLogger(__name__)
PALERT = "Phone not valid: Phone number must contain only digits! And length min 10, max 15!"
EALERT = "Email not valid: must be a well-formed email address"

@pytest.mark.smoke
@pytest.mark.parametrize("c", [create_contact(), create_contact(description="")])
def test_add_c_success(authenticated_driver, c):
    logger.info(f"Starting test_add_c_success with contact: {c.name} {c.last_name}, phone: {c.phone}")
    cp, csp = ContactPage(authenticated_driver), ContactsPage(authenticated_driver)
    cp.create_contact_steps(c)
    assert csp.contact_card_visible(c.phone)

@pytest.mark.regression
@pytest.mark.parametrize("c, err, is_a", [
    (create_contact(phone="05##"), "Phone not valid:", True),
    (create_contact(email="w.com"), "Email not valid:", True),
    (create_contact(name=""), None, False),
    (create_contact(last_name=""), None, False),
    (create_contact(address=""), None, False),
    (create_contact(phone="fghjfghdf"), PALERT, True),
    (create_contact(email="invalidemail"), EALERT, True)
])
def test_add_c_neg(authenticated_driver, c, err, is_a):
    logger.info(f"Starting test_add_c_neg with phone: {c.phone}, expected alert: {is_a}")
    cp, csp = ContactPage(authenticated_driver), ContactsPage(authenticated_driver)
    cp.open_add_contact_form()
    cp.fill_contact_form(c)
    cp.submit_contact()
    if is_a:
        assert err in cp.get_alert_text()
        cp.accept_alert()
    else:
        assert cp.is_add_btn_active()
        cp.open_contacts_link()
        assert csp.contact_cards_count(c.phone) == 0

@pytest.mark.regression
@pytest.mark.xfail(reason="Not implemented")
def test_add_c_empty_email(authenticated_driver):
    logger.info("Starting test_add_c_empty_email")
    cp, csp = ContactPage(authenticated_driver), ContactsPage(authenticated_driver)
    c = create_contact(email="")
    cp.open_add_contact_form()
    cp.fill_contact_form(c)
    cp.submit_contact()
    assert cp.is_add_btn_active()
    cp.open_contacts_link()
    assert csp.contact_card_visible(c.phone) == 0

@pytest.mark.regression
@pytest.mark.skip(reason="Not implemented")
def test_add_c_dup_phone(authenticated_driver):
    logger.info("Starting test_add_c_dup_phone")
    cp, csp = ContactPage(authenticated_driver), ContactsPage(authenticated_driver)
    c = create_contact()
    cp.create_contact_steps(c)
    assert csp.contact_card_visible(c.phone)
    c2 = create_contact(phone=c.phone)
    cp.open_add_contact_form()
    cp.fill_contact_form(c2)
    cp.submit_contact()
    csp.open_contacts_link()
    assert csp.contact_cards_count(c.phone) == 1




