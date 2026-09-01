
from faker import Faker

from models.user import User

fake = Faker()
def create_user(username = None, password = None):
    return User(username=username if username is not None else fake.unique.email(),
                password=password if password is not None else fake.password(
                    length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
                ))

EXITING_USER_EMAIL = "testdima@gmail.com"
EXITING_USER_PASSWORD = "Test@123456"
INVALID_EMAIL = "testdima@gmail"
INVALID_PASSWORD = "Test1"

def exiting_user():
    return create_user(EXITING_USER_EMAIL, EXITING_USER_PASSWORD)

def invalid_email_user():
    return create_user(INVALID_EMAIL, EXITING_USER_PASSWORD)

def invalid_password_user():
    return create_user(EXITING_USER_EMAIL, INVALID_PASSWORD)