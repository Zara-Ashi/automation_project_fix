from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utils.helpers import unique_email, unique_login


def test_TC_AUTH_01_registration(page):
    registration_page = RegistrationPage(page)

    email = unique_email()
    login = unique_login()

    registration_page.register(email, login)

    assert registration_page.is_registered_successfully()


def test_TC_AUTH_02_login(page):
    login_page = LoginPage(page)
    account_page = AccountPage(page)

    login_page.open()
    login_page.login("zaza_jura", "Zara9559!")

    account_page.should_be_opened()
    account_page.is_account_label_visible()