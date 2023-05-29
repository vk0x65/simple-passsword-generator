import random
import string
import pyperclip

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!" + "#" + "@" + "$" + "_"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password_count = int(input('Enter how many password digits you want: '))
password = generate_password(password_count)
pyperclip.copy(password)
print(password)
