import csv
from contact import Contact

FILE_NAME = "contacts.csv"

def load_contacts():
    contacts = []
    try:
        with open(FILE_NAME, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                contacts.append(Contact.from_dict(row))
    except FileNotFoundError:
        print("CSV file not found!!!!!!!!!")
    return contacts

def save_contacts(contacts):
    with open(FILE_NAME, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["name", "phone", "email", "address"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact.to_dict())