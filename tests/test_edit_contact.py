import time
import logging
import pytest
from data.contact_data import create_contact, fake
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage

logger = logging.getLogger(__name__)

@pytest.mark.smoke
def test_edit_name(authenticated_driver):
    logger.info("Starting test_edit_name")
    cp, csp = ContactPage(authenticated_driver), ContactsPage(authenticated_driver)
    c = create_contact()
    cp.create_contact_steps(c)
    nn = fake.first_name()
    csp.open_contact_details(c.phone)
    csp.open_edit_mode()
    csp.set_edit_field(csp.EDIT_NAME_INPUT, nn)
    csp.submit_edit()
    assert csp.contact_name_for_phone(c.phone) == nn

@pytest.mark.regression
@pytest.mark.parametrize("field, val_fn", [
    (ContactsPage.EDIT_LAST_NAME_INPUT, lambda: fake.last_name()),
    (ContactsPage.EDIT_PHONE_INPUT, lambda: fake.unique.numerify("05########")),
    (ContactsPage.EDIT_EMAIL_INPUT, lambda: fake.unique.email()),
    (ContactsPage.EDIT_ADDRESS_INPUT, lambda: fake.city())
])
def test_edit_fields(authenticated_driver, field, val_fn):
    logger.info(f"Starting test_edit_fields for field: {field}")
    cp, csp = ContactPage(authenticated_driver), ContactsPage(authenticated_driver)
    c = create_contact()
    cp.create_contact_steps(c)
    nv = val_fn()
    csp.open_contact_details(c.phone)
    csp.open_edit_mode()
    csp.set_edit_field(field, nv)
    csp.submit_edit()
    if field == ContactsPage.EDIT_PHONE_INPUT:
        assert csp.contact_card_visible(nv)
    else:
        csp.open_contact_details(c.phone)
        csp.open_edit_mode()
        assert csp.get_edit_contact(field) == nv

@pytest.mark.regression
@pytest.mark.skip(reason="Not implemented")
def test_edit_desc(authenticated_driver):
    logger.info("Starting test_edit_desc")
    cp, csp = ContactPage(authenticated_driver), ContactsPage(authenticated_driver)
    c = create_contact()
    cp.create_contact_steps(c)
    nd = fake.sentence(5)
    csp.open_contact_details(c.phone)
    csp.open_edit_mode()
    csp.set_edit_field(csp.EDIT_DESCRIPTION_INPUT, nd)
    csp.submit_edit()
    csp.open_contact_details(c.phone)
    csp.open_edit_mode()
    assert csp.get_edit_contact(csp.EDIT_DESCRIPTION_INPUT) == nd

@pytest.mark.regression
@pytest.mark.parametrize("field, expected_attr", [
    (ContactsPage.EDIT_NAME_INPUT, "name"),
    (ContactsPage.EDIT_LAST_NAME_INPUT, "last_name"),
    (ContactsPage.EDIT_EMAIL_INPUT, "email"),
    (ContactsPage.EDIT_ADDRESS_INPUT, "address"),
    (ContactsPage.EDIT_PHONE_INPUT, "phone")
])
def test_edit_empty_neg(authenticated_driver, field, expected_attr):
    logger.info(f"Starting test_edit_empty_neg for field: {field}")
    cp, csp = ContactPage(authenticated_driver), ContactsPage(authenticated_driver)
    c = create_contact()
    cp.create_contact_steps(c)
    csp.open_contact_details(c.phone)
    csp.open_edit_mode()
    csp.set_edit_field(field, "")
    csp.submit_edit()
    if field == ContactsPage.EDIT_NAME_INPUT:
        assert csp.contact_name_for_phone(c.phone) == getattr(c, expected_attr)
    else:
        assert csp.contact_cards_count(c.phone) == 1
        if field != ContactsPage.EDIT_PHONE_INPUT:
            csp.open_contact_details(c.phone)
            csp.open_edit_mode()
            assert csp.get_edit_contact(field) == getattr(c, expected_attr)

@pytest.mark.regression
def test_edit_dup_email_neg(authenticated_driver):
    logger.info("Starting test_edit_dup_email_neg")
    cp, csp = ContactPage(authenticated_driver), ContactsPage(authenticated_driver)
    c1, c2 = create_contact(), create_contact()
    cp.create_contact_steps(c1)
    cp.create_contact_steps(c2)
    csp.open_contact_details(c2.phone)
    csp.open_edit_mode()
    csp.set_edit_field(csp.EDIT_EMAIL_INPUT, c1.email)
    csp.submit_edit()
    csp.open_contact_details(c2.phone)
    csp.open_edit_mode()
    assert csp.get_edit_contact(csp.EDIT_EMAIL_INPUT) == c2.email






