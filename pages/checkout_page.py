from playwright.sync_api import expect

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.guest_radio = page.locator("input[value='guest']")
        self.continue_btn = page.locator("button:has-text('Continue')")
        self.confirm_order_btn = page.locator("button:has-text('Confirm Order')")
        self.guest_firstname = page.locator("#guestFrm_firstname")
        self.guest_lastname = page.locator("#guestFrm_lastname")
        self.guest_email = page.locator("#guestFrm_email")
        self.guest_address = page.locator("#guestFrm_address_1")
        self.guest_city = page.locator("#guestFrm_city")
        self.guest_country = page.locator("#guestFrm_country_id")
        self.guest_postcode = page.locator("#guestFrm_postcode")

    def select_guest_checkout(self):
        if self.guest_radio.count() > 0:
            self.guest_radio.check()
            self.continue_btn.click()

    def fill_guest_form(self, first_name, last_name, email, address, city, country, postcode):
        if self.guest_firstname.is_visible():
            self.guest_firstname.fill(first_name)
            self.guest_lastname.fill(last_name)
            self.guest_email.fill(email)
            self.guest_address.fill(address)
            self.guest_city.fill(city)
            self.guest_country.select_option(label=country)
            self.guest_postcode.fill(postcode)
            self.continue_btn.click()

    def confirm_order(self):
        if self.confirm_order_btn.count() > 0:
            self.confirm_order_btn.click()

    def should_show_checkout_confirmation(self):
        expect(self.page.locator("body")).to_contain_text("Checkout")
