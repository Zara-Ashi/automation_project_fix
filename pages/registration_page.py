from pages.base_page import BasePage
from utils.config import BASE_URL


class RegistrationPage(BasePage):
    URL = f"{BASE_URL}/index.php?rt=account/create"

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

    def fill_form(self, email, login, password="Test1234!"):
        self.firstname.fill("Auto")
        self.lastname.fill("Tester")
        self.email.fill(email)
        self.telephone.fill("1234567890")
        self.address.fill("Test Address")
        self.city.fill("Test City")
        self.country.select_option("United States")
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
        self.page.wait_for_load_state("networkidle")

    def register(self, email, login, password="Test1234!"):
        self.open()
        self.fill_form(email, login, password)
        self.submit()

    def is_registered_successfully(self):
        content = self.page.content().lower()
        return (
            "your account has been created" in content
            or "account/success" in self.page.url
            or "account" in self.page.url
        )
