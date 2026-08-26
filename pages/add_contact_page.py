from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class ContactPage(BasePage):
    ADD_CONTACT_LINK = (By.CSS_SELECTOR, 'a[href="/add"]')
    NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Name"]')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
    PHONE_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Phone"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[placeholder="email"]')
    ADDRESS_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Address"]')
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, 'input[placeholder="description"]')
    SAVE_BTN = (By.XPATH, '//button[b[text()="Save"]]')
    CONTACTS_LINK = (By.CSS_SELECTOR, 'a[href="/contacts"]')


    # def __init__(self, driver):
    #     self.driver = driver

    def open_add_contact_form(self):
        # self.driver.find_element(*self.ADD_CONTACT_LINK).click()
        self.click(self.ADD_CONTACT_LINK)

    def fill_name(self, name: str):
        # self.driver.find_element(*self.NAME_INPUT).clear()
        # self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.fill(self.NAME_INPUT, name)

    def fill_last_name(self, last_name: str):
        # self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        # self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.fill(self.LAST_NAME_INPUT, last_name)

    def fill_phone(self, phone: str):
        # self.driver.find_element(*self.PHONE_INPUT).clear()
        # self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.fill(self.PHONE_INPUT, phone)

    def fill_email(self, email: str):
        # self.driver.find_element(*self.EMAIL_INPUT).clear()
        # self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.fill(self.EMAIL_INPUT, email)

    def fill_address(self, address: str):
        # self.driver.find_element(*self.ADDRESS_INPUT).clear()
        # self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)
        self.fill(self.ADDRESS_INPUT, address)

    def fill_description(self, description: str):
        # self.driver.find_element(*self.DESCRIPTION_INPUT).clear()
        # self.driver.find_element(*self.DESCRIPTION_INPUT).send_keys(description)
        self.fill(self.DESCRIPTION_INPUT, description)

    def fill_contact_form(self, contact):
        self.fill_name(contact.name)
        self.fill_last_name(contact.last_name)
        self.fill_phone(contact.phone)
        self.fill_email(contact.email)
        self.fill_address(contact.address)
        self.fill_description(contact.description)

    def submit_contact(self):
        # self.driver.find_element(*self.SAVE_BTN).click()
        self.click(self.SAVE_BTN)

    def contact_card_visible(self, phone):
        locator = (By.XPATH, f'//h3[text()="{phone}"]')
        try:
            element = WebDriverWait(self.driver,2).until(
            EC.visibility_of_element_located(locator)
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    def open_contact_details(self,phone):
        card = self.driver.find_element(By.XPATH, f'//h3[text()="{phone}"]/..')
        card.click()

    def open_contacts_link(self):
        self.click(self.CONTACTS_LINK)