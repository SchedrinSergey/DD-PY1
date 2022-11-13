import random
import string
def get_random_password(n=8) -> str:
    up_letters = string.ascii_uppercase
    low_letters = string.ascii_lowercase
    digits = string.digits
    combined_string = up_letters + low_letters + digits
    password_list = random.sample(combined_string, n)
    password = "".join(password_list)
    return password


print(get_random_password())
