
# Python Phonebook Manager

A **console-based phonebook manager** written in Python.  
It allows you to **add, view, search, update, and delete contacts** with multiple phone numbers and optional emails. Contacts are stored in a JSON file (`contacts.json`).

---

## Features

- Add a new contact with multiple phone numbers and optional email.
- View all saved contacts.
- Search contacts by **name** or **phone number**.
- Update existing contacts (add/update/delete phone numbers, update email).
- Delete contacts.
- Persistent storage using JSON.

---

## Requirements

- Python 3.x
- No external libraries required (`json` and `os` are built-in).

---

## How It Works

1. **Load Contacts:** Loads existing contacts from `contacts.json` if it exists.
2. **Main Menu:** Provides options to manage contacts.
3. **Add Contact:** Enter name, phone numbers with labels (home, mobile, etc.), and optional email.
4. **View Contacts:** Lists all contacts with their phone numbers and emails.
5. **Search Contact:** By name (exact match) or phone number (checks all labels).
6. **Update Contact:** Add/update/delete phone numbers or update email.
7. **Delete Contact:** Removes a contact permanently.
8. **Save Contacts:** Automatically saves all changes to `contacts.json`.

---

## Code Overview

### Load & Save Contacts
```python
import json, os

PHONEBOOK_FILE = "contacts.json"

# Load existing contacts
if os.path.exists(PHONEBOOK_FILE):
    with open(PHONEBOOK_FILE, "r") as file:
        contacts = json.load(file)
else:
    contacts = {}

# Save contacts to file
def save_contacts():
    with open(PHONEBOOK_FILE, "w") as file:
        json.dump(contacts, file, indent=4)
````

### Add a Contact

```python
def add_contact():
    name = input("Enter contact name: ").strip()
    if not name or name in contacts:
        print("❌ Invalid or duplicate name")
        return
    phones = {}
    while True:
        label = input("Enter phone label: ").strip().lower()
        phone = input(f"Enter {label} number: ").strip()
        if phone.isdigit():
            phones[label] = phone
        more = input("Add another number? (y/n): ").strip().lower()
        if more != "y":
            break
    email = input("Enter email (optional): ").strip()
    contacts[name] = {"phones": phones, "email": email}
    save_contacts()
    print(f"✅ Contact '{name}' added!")
```

### Search by Name

```python
def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        phones = ", ".join([f"{label}: {num}" for label, num in info["phones"].items()])
        print(f"Found: {name}, Phones: [{phones}], Email: {info['email']}")
    else:
        print(f"No contact found with name '{name}'")
```

### Search by Phone

```python
def search_by_phone():
    phone = input("Enter phone to search: ").strip()
    found = False
    for name, info in contacts.items():
        for label, num in info["phones"].items():
            if num == phone:
                print(f"Found: {name}, Label: {label}, Phone: {num}, Email: {info['email']}")
                found = True
    if not found:
        print(f"No contact found with phone '{phone}'")
```

### Update Contact

```python
def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contacts:
        info = contacts[name]
        # Update phones
        while True:
            action = input("[a]dd, [u]pdate, [d]elete, [q]uit: ").strip().lower()
            if action == "a":
                label = input("New label: ").strip().lower()
                phone = input(f"Number for {label}: ").strip()
                info["phones"][label] = phone
            elif action == "u":
                label = input("Label to update: ").strip().lower()
                phone = input("New number: ").strip()
                info["phones"][label] = phone
            elif action == "d":
                label = input("Label to delete: ").strip().lower()
                del info["phones"][label]
            elif action == "q":
                break
        # Update email
        email = input("New email (leave blank to keep): ").strip()
        if email:
            info["email"] = email
        save_contacts()
        print(f"✅ Contact '{name}' updated!")
        # Delete if no phones left
        if not info["phones"]:
            choice = input("No phones left. Delete contact? (y/n): ").strip().lower()
            if choice == "y":
                del contacts[name]
                save_contacts()
                print(f"🗑️ Contact '{name}' deleted")
```

### Delete Contact

```python
def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"🗑️ Contact '{name}' deleted!")
```

---

## How to Run

```bash
python app.py
```

* Follow the on-screen menu.
* Contacts are automatically saved in `contacts.json`.

---

## Possible Improvements

* Add a **GUI interface** with Tkinter or PyQt.
* Allow **partial match searches**.
* Enable **sorting contacts** by name or label.
* Encrypt `contacts.json` for **privacy**.
* Add **CSV import/export**.
* Add **backup and restore** functionality.

---

## License

MIT License

```

This merges all necessary explanations, usage instructions, code snippets, and improvement ideas so you can copy-paste directly as a `README.md`.  

If you want, I can also **include the full Python code in the MD file itself** under a single section, so someone can just copy it and run without touching anything else. Do you want me to do that?
```
