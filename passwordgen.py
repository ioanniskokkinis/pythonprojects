import string
import random

length = int(input("Πόσους χαρακτήρες θέλεις στον κωδικό σου; "))

all_characters = string.ascii_letters + string.digits + string.punctuation

password = ""
!
for i in range(length):
    char = random.choice(all_characters)
    password = password + char

print("Ο νέος σου κωδικός είναι:", password)
