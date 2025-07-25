# Contact Book CLI System

This is a simple **Command Line Interface (CLI)** Contact Book Management System built using basic Python. It allows users to manage their personal contacts directly from the terminal — without any advanced libraries or frameworks.

---

## 🔧 Features

### 1. Add Contact
- Input Name, Phone Number, Email, and Address.
- Validates each input:
  - Name: Only letters and spaces (min 2 characters)
  - Phone: Must be in format `+880XXXXXXXXXX`
  - Email: Must include `@` and a domain like `.com`
- Prevents duplicate phone numbers.
- Automatically saves to a file.

### 2. View Contacts
- Lists all saved contacts in a neat format.

### 3. Search Contact
- Search contacts by name, email, or phone.
- Displays matching results.

### 4. Remove Contact
- Deletes a contact using their phone number.
- Asks for confirmation before deletion.

### 5. Exit
- Safely exits the program.

---

##  Data Handling

- All contacts are stored in `contacts.csv`.
- Data is automatically loaded when the program starts and saved when updated.

---

##  Input Validations

| Field   | Validation Rules                               |
|---------|------------------------------------------------|
| Name    | Only alphabets and spaces, min 2 characters    |
| Phone   | Starts with `+880`, followed by 11 digits      |
| Email   | Must include `@` and a domain (e.g. `.com`)    |
| Address | Any text                                       |

---

## File Structure

```bash
contact_book_cli/
├── main.py             # Main program file with CLI menu
├── contact.py          # Handles Contact class and validation
├── contact_manager.py  # Adds, searches, removes contacts
├── file_handler.py     # Handles loading/saving from CSV
├── contacts.csv        # Stores all contact data
└── README.md           # Project documentation
```
---

##  How to Setup and Run This Project

### Clone the Repository
```bash
git clone https://github.com/MuHIUDDIn98/Contact_Book_MANAGEMENT_CLI_SYSTEM.git

```

```bash
cd contact_book_cli
```

### Create a Virtual Environment (Optional but Recommended)
🧪 A virtual environment keeps your project dependencies isolated.

```bash

python -m venv venv
venv\Scripts\activate
```

### installing dependencies


### Learning Goals
This project helps you understand:

File handling with csv

Input validation

Functions and classes

Modular programming

Building menu-driven CLI programs in Python


