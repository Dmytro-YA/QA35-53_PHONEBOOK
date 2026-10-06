import time
import logging
import pytest
from pages.contacts_page import ContactsPage

logger = logging.getLogger(__name__)

@pytest.mark.regression
def test_del_c(ensure_min_contacts):
    logger.info("Starting test_del_c: deleting a single contact")
    csp = ContactsPage(ensure_min_contacts)
    csp.open_contacts_link()
    b4 = csp.total_contacts_count()
    time.sleep(1)
    csp.open_first_contact()
    csp.remove_current_contact()
    assert b4 - 1 == csp.total_contacts_count()

@pytest.mark.regression
def test_del_all(ensure_min_contacts):
    logger.info("Starting test_del_all: deleting all contacts")
    csp = ContactsPage(ensure_min_contacts)
    csp.open_contacts_link()
    csp.remove_all_contacts()
    assert csp.total_contacts_count() == 0

