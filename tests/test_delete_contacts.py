import time

from pages.contacts_page import ContactsPage
import logging
logger = logging.getLogger(__name__)

def test_delete_contact_decreases_list_by_one(ensure_min_contacts):
    logger.info("Start test_delete_contact_decreases_list_by_one")
    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contacts_link()
    count_before = contacts_page.total_contacts_count()
    logger.info(f"There are {count_before} contacts before deletion")
    time.sleep(1)
    contacts_page.open_first_contact()
    contacts_page.remove_current_contact()
    count_after = contacts_page.total_contacts_count()
    logger.info(f"There are {count_after} contacts after deletion")
    assert count_before - 1 == count_after

def test_remove_all_contacts(ensure_min_contacts):
    contacts_page = ContactsPage(ensure_min_contacts)
    contacts_page.open_contacts_link()
    contacts_page.remove_all_contacts()
    assert contacts_page.total_contacts_count() == 0

