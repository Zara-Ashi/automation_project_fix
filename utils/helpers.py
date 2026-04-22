from faker import Faker

fake = Faker()


def unique_email():
    return fake.email()


def unique_login():
    return fake.user_name()