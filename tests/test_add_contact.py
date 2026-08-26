import random

from models.contact import Contact
from pages.add_contact_page import ContactPage
from faker import Faker

from pages.faker1 import faker


def test_add_contact_success_all_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    random_suffix = random.randint(1, 1000000)

    contact = Contact(
        faker.name(),
        faker.last_name(),
        faker.unique.numerify("05########"),
        faker.unique.email(),
        faker.address(),
        faker.sentence(5)
    )
    print(random_suffix)
    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)

def test_add_contact_success_required_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    random_suffix = random.randint(1, 1000000)

    contact = Contact(
        faker.name(),
        faker.last_name(),
        faker.unique.numerify("05########"),
        faker.unique.email(),
        faker.address(),
        ""
    )
    print(random_suffix)
    contact_page.open_add_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)