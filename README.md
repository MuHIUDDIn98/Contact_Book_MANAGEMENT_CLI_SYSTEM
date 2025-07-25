# Contact Book CLI System

This is a simple **Command Line Interface (CLI)** Contact Book Management System built using basic Python. It allows users to manage their personal contacts directly from the terminal — without any advanced libraries or frameworks.

---

##  Features

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

- All contacts are stored in `contacts.csv`
- Data is automatically loaded when the program starts and saved when updated.

---

##  Input Validations

| Field     | Validation Rules                               |
|-----------|------------------------------------------------|
| Name      | Only alphabets and spaces, min 2 characters    |
| Phone     | Starts with `+880`, followed by 11 digits      |
| Email     | Must include `@` and a domain (e.g. `.com`)    |
| Address   | Any text                                        |

---

## File Structure

```
contact_book_cli/
├── main.py               # Main program file with CLI menu
├── contact.py            # Handles Contact class and validation
├── contact_manager.py    # Adds, searches, removes contacts
├── file_handler.py       # Handles loading/saving from CSV
├── contacts.csv          # Stores all contact data
├── README.md             # Project documentation
```

---

##  How to Run

1. Make sure you have Python installed.
2. Unzip the project folder.
3. Open your terminal or command prompt.
4. Navigate to the folder.
5. Run:

```bash
python main.py
```

---

##  Learning Goals

This project helps you understand:
- File handling (`csv`)
- Functions and classes
- Input validation
- Modular programming
- Menu-driven CLI programs

---

## ✅ No External Libraries Used
Only Python's built-in modules are used. It's perfect for beginners!

---

Enjoy building your Contact Book! 📖
