import string
import random

# 1. Ζητάμε το μήκος από τον χρήστη
length = int(input("Πόσους χαρακτήρες θέλεις στον κωδικό σου; "))

all_characters = string.ascii_letters + string.digits + string.punctuation

password = ""

# 3. Το loop που έγραψες!
for i in range(length):
    char = random.choice(all_characters)
    password = password + char

print("Ο νέος σου κωδικός είναι:", password)