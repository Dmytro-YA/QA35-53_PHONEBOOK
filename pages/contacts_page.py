import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from pages.base_page import BasePage

logger = logging.getLogger(__name__)
class ContactsPage(BasePage):
    CONTACTS_LINK = (By.CSS_SELECTOR, 'a[href="/contacts"]')
    CONTACT_CARDS = (By.CSS_SELECTOR, '.contact-item_card__2SOIM')
    EDIT_BTN = (By.XPATH, '//button[text()="Edit"]')
    EDIT_NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Name"]')
    EDIT_LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
    EDIT_PHONE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Phone"]')
    EDIT_EMAIL_INPUT = (By.CSS_SELECTOR, 'input[placeholder="email"]')
    EDIT_ADDRESS_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Address"]')
    EDIT_DESCRIPTION_INPUT = (By.CSS_SELECTOR, 'input[placeholder="desc"]')
    EDIT_SAVE_BTN = (By.XPATH, '//button[text()="Save"]')
    REMOVE_BTN = (By.XPATH, '//button[text()="Remove"]')



    def open_contacts_link(self):
        self.click(self.CONTACTS_LINK)
        # WebDriverWait(self.driver,5).until(EC.url_contains("contacts"))
        self.wait_until_url_matches(r"/contacts$")

    def contact_cards_count(self, phone):
        return len(self.driver.find_elements(By.XPATH,f"//h3[text()='{phone}']/.."))

    def open_contact_details(self, phone):
        locator = (By.XPATH, f"//div[contains(@class, 'contact-item_card')][.//h3[text()='{phone}']]")
        self.click(locator)

    def contact_card_visible(self, phone):
        locator = (By.XPATH, f'//h3[text()="{phone}"]')
        try:
            # element = WebDriverWait(self.driver,2).until(
            # EC.visibility_of_element_located(locator)
            # )
            # return element.is_displayed()
            return self.wait_until_visible(locator).is_displayed()
        except TimeoutException:
            return False

    def open_edit_mode(self):
        self.click(self.EDIT_BTN)

    def set_edit_field(self, locator, value):
        self.fill(locator, value)

    def submit_edit(self):
        self.click(self.EDIT_SAVE_BTN)
        WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(self.EDIT_SAVE_BTN))

    def contact_name_for_phone(self, phone):
        card = self.driver.find_element(By.XPATH, f"//div[contains(@class, 'contact-item_card')][.//h3[text()='{phone}']]")
        return card.find_element(By.TAG_NAME, "h2").text

    def get_edit_contact(self, locator):
        return self.find(locator).get_attribute("value")

    def remove_current_contact(self):
        logger.info("Removing current contact")
        self.click(self.REMOVE_BTN)
        # time.sleep(1)
        self.wait_until_url_matches(r"/contacts$")

    def open_first_contact(self):
        cards = self.driver.find_elements(*self.CONTACT_CARDS)
        first_card = cards[0]
        first_card.click()

    def total_contacts_count(self):
        return len(self.driver.find_elements(*self.CONTACT_CARDS))

    def remove_all_contacts(self):
        while self.total_contacts_count() > 0:
            self.open_first_contact()
            self.remove_current_contact()




