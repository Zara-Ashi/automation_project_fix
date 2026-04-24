import re
from playwright.sync_api import expect
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.guest_option = page.locator("#guest")
        self.returning_option = page.locator("#login")

        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.email = page.locator("#email")
        self.address = page.locator("#address")
        self.city = page.locator("#city")
        self.country = page.locator("#country")
        self.postcode = page.locator("#postcode")

        self.confirm_button = page.locator("#confirm")
        self.error = page.locator(".error")

    def select_guest_checkout(self):
        self.guest_option.click()

    def fill_guest_form(self, first, last, email, address, city, country, postcode):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.email.fill(email)
        self.address.fill(address)
        self.city.fill(city)
        self.country.fill(country)
        self.postcode.fill(postcode)

    def confirm_order(self):
        self.confirm_button.click()

    def verify_checkout_confirmation(self):
        expect(self.page).to_have_url(re.compile("success"))

    def verify_guest_option(self):
        expect(self.guest_option).to_be_visible()

    def verify_returning_customer_option(self):
        expect(self.returning_option).to_be_visible()

    def verify_validation_errors(self):
        expect(self.error).to_be_visible()

    def verify_email_error(self):
        expect(self.error).to_contain_text("email")

    def verify_regions_updated(self):
        expect(self.page.locator("#region")).to_be_visible()

    def verify_not_empty(self):
        expect(self.page.locator(".cart-item")).not_to_have_count(0)

    def verify_success_url(self):
        expect(self.page).to_have_url(re.compile("success"))

    def verify_order_number(self):
        expect(self.page.locator(".order-number")).to_be_visible()