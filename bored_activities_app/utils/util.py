import random, string
import re

EMAIL_RULE = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
PASSWORD_RULE = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

def random_string_generator(length = 32):
    return ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))

def password_validation(password):
    password_rule = re.compile(PASSWORD_RULE)
    return re.search(password_rule, password)


def email_validation(email):
    return re.fullmatch(EMAIL_RULE, email)

