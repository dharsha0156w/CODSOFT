import random
import string
try:
    length = int(input("Enter the desired length of the password: "))
    if length < 1:
        print("Password length must be at least 1.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number for the password length.")
