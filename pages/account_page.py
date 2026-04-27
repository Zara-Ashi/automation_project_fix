from playwright.sync_api import expect

from pages.base_page import BasePage


class AccountPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.account_label = page.locator("text=My Account")

    def should_be_opened(self):
        expect(self.page).to_have_url(lambda url: "login" not in url)

    def is_account_label_visible(self):
        expect(self.account_label).to_be_visible()
