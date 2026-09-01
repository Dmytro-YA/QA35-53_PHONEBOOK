import random
import time

import pytest

from data.contact_data import create_contact
from models.contact import Contact
from pages import contacts_page
from pages.add_contact_page import ContactPage
from faker import Faker

from pages.contacts_page import ContactsPage
from pages.faker1 import faker


def test_add_contact_success_all_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactPage(authenticated_driver)
    contact = create_contact()

    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contacts_page.contact_card_visible(contact.phone)

def test_add_contact_success_required_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact(description="")

    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)


def test_add_contact_with_invalid_phone(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contact = Contact(
        faker.name(),
        faker.last_name(),
        faker.unique.numerify("05##"),
        faker.unique.email(),
        faker.address(),
        faker.sentence(5)
    )
    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert "Phone not valid:" in contact_page.get_alert_text()
    print(contact_page.get_alert_text())
    time.sleep(2)
    contact_page.accept_alert()

def test_add_contact_with_invalid_email(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contact = Contact(
        faker.name(),
        faker.last_name(),
        faker.unique.numerify("05##########"),
        "w.com",
        faker.address(),
        faker.sentence(5)
    )
    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert "Email not valid:" in contact_page.get_alert_text()
    print(contact_page.get_alert_text())
    time.sleep(2)
    contact_page.accept_alert()

def test_add_contact_empty_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)


    contact = Contact(
        "",
        faker.last_name(),
        faker.unique.numerify("05########"),
        faker.unique.email(),
        faker.address(),
        faker.sentence(5)
    )

    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    contact_page.open_contacts_link()


    assert not contact_page.contact_card_visible(contact.phone)


def test_add_contact_empty_last_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        faker.name(),
        "",
        faker.unique.numerify("05########"),
        faker.unique.email(),
        faker.address(),
        faker.sentence(5)
    )

    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    contact_page.open_contacts_link()

    assert not contact_page.contact_card_visible(contact.phone)

def test_add_contact_empty_address(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        faker.name(),
        faker.last_name(),
        faker.unique.numerify("05########"),
        faker.unique.email(),
        "",
        faker.sentence(5)
    )

    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    contact_page.open_contacts_link()

    assert not contact_page.contact_card_visible(contact.phone)


PHONE_ALERT_TEXT = "Phone not valid: Phone number must contain only digits! And length min 10, max 15!"
EMAIL_ALERT_TEXT = "Email not valid: must be a well-formed email address"

def test_add_contact_empty_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactPage(authenticated_driver)
    contact = create_contact(name="")



    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_btn_active()
    contact_page.open_contacts_link()

    assert contacts_page.contact_cards_count(contact.phone) == 0

def test_add_contact_empty_last_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactPage(authenticated_driver)
    contact = create_contact(last_name="")



    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_btn_active()
    contact_page.open_contacts_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0


# @pytest.mark.skip(reason="Not implemented yet")
@pytest.mark.xfail(reason="Not implemented yet")
def test_add_contact_empty_email(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)


    contact = Contact(
        faker.name(),
        faker.last_name(),
        faker.unique.numerify("05########"),
        "",
        faker.address(),
        faker.sentence(5)
    )

    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_btn_active()
    contact_page.open_contacts_link()
    assert contact_page.contact_card_visible(contact.phone) == 0



def test_add_contact_empty_address(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactPage(authenticated_driver)
    contact = create_contact(address="")



    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.is_add_btn_active()
    contact_page.open_contacts_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0

def test_add_contact_invalid_phone(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactPage(authenticated_driver)
    contact = create_contact(phone="fghjfghdf")



    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
    contact_page.accept_alert()

    assert contact_page.is_add_btn_active()
    contact_page.open_contacts_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0

def test_add_contact_invalid_email(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactPage(authenticated_driver)
    contact = create_contact(email="invalidemail")



    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.get_alert_text().strip() == EMAIL_ALERT_TEXT
    contact_page.accept_alert()

    assert contact_page.is_add_btn_active()
    contact_page.open_contacts_link()
    assert contacts_page.contact_cards_count(contact.phone) == 0

@pytest.mark.skip(reason="Not implemented yet")
def test_add_contact_duplicate_phone_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactPage(authenticated_driver)

    shared_phone = faker.unique.numerify("05########")
    first_contact = create_contact(phone=shared_phone)
    second_contact = create_contact(phone=shared_phone)

    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(first_contact)
    contact_page.submit_contact()
    assert contacts_page.contact_card_visible(shared_phone)

    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(second_contact)
    contact_page.submit_contact()


    contacts_page.open_contacts_link()
    assert contacts_page.contact_cards_count(shared_phone) == 1




