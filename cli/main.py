import csv
from datetime import datetime
import os

# Ορίζουμε το όνομα του αρχείου
FILE_NAME = 'expenses.csv'

# 1. Παίρνουμε τα δεδομένα από τον χρήστη
task = input("Περιγραφή εξόδου: ")
amount = input("Ποσό: ")
category = input("Κατηγορία (π.χ. Τρόφιμα, Μεταφορές): ")
date = datetime.now().strftime("%d-%m-%Y %H:%M") 

with open(FILE_NAME, 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow([date, task, amount, category])

print(f"✅ Η εγγραφή '{task}' αποθηκεύτηκε!")