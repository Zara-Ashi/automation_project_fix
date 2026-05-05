from pages.base_page import BasePage
from utils.config import URLS, DEFAULT_PASSWORD
from playwright.sync_api import expect


class RegistrationPage(BasePage):
    URL = URLS["registration"]

    def __init__(self, page):
        super().__init__(page)
        self.firstname = page.locator("#AccountFrm_firstname")
        self.lastname = page.locator("#AccountFrm_lastname")
        self.email = page.locator("#AccountFrm_email")
        self.telephone = page.locator("#AccountFrm_telephone")
        self.address = page.locator("#AccountFrm_address_1")
        self.city = page.locator("#AccountFrm_city")
        self.country = page.locator("#AccountFrm_country_id")
        self.zone = page.locator("#AccountFrm_zone_id")
        self.postcode = page.locator("#AccountFrm_postcode")
        self.loginname = page.locator("#AccountFrm_loginname")
        self.password = page.locator("#AccountFrm_password")
        self.confirm = page.locator("#AccountFrm_confirm")
        self.agree_checkbox = page.locator("#AccountFrm_agree")
        self.submit_btn = page.locator("button[title='Continue']")

    def open(self):
        self.page.goto(self.URL)
        expect(self.firstname).to_be_visible()

    def fill_form(self, email, login, password=DEFAULT_PASSWORD):
        self.firstname.fill("Auto")
        self.lastname.fill("Tester")
        self.email.fill(email)
        self.telephone.fill("1234567890")
        self.address.fill("Test Address")
        self.city.fill("Test City")
        self.country.select_option(label="United States")
        self.page.wait_for_function(
            "document.querySelectorAll('#AccountFrm_zone_id option').length > 1"
        )
        self.zone.select_option(label="California")
        self.postcode.fill("12345")
        self.loginname.fill(login)
        self.password.fill(password)
        self.confirm.fill(password)
        self.agree_checkbox.check()

    def submit(self):
        self.submit_btn.click()
        expect(self.page).to_have_url(lambda url: "success" in url or "account" in url)

    def register(self, email, login, password=DEFAULT_PASSWORD):
        self.open()
        self.fill_form(email, login, password)
        self.submit()