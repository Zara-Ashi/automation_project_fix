import time


def unique_email():
    return f"testuser_{int(time.time())}@mail.com"


def unique_login():
    return f"user_{int(time.time())}"
