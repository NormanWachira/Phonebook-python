import json
import os

PHONEBOOK_FILE = "contacts.json"

# Load existing contacts from file (if any)
if os.path.exists(PHONEBOOK_FILE):
    with open(PHONEBOOK_FILE, "r") as file:
        contacts = json.load(file)
else:
    contacts = {}

# Save contacts to file
def save_contacts():
    with open(PHONEBOOK_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = input("Enter contact name: ").strip()

    if not name:
        print("❌ Name cannot be empty!")
        return

    if name in contacts:
        print(f"❌ Contact '{name}' already exists.")
        return

    phones = {}
    while True:
        label = input("Enter phone label (e.g. home, work, mobile): ").strip().lower()
        phone = input(f"Enter {label} phone number: ").strip()

        if not phone.isdigit():
            print("❌ Phone number must contain digits only!")
            continue

        phones[label] = phone

        more = input("Add another number? (y/n): ").strip().lower()
        if more != "y":
            break

    email = input("Enter email address (optional): ").strip()
    if email and "@" not in email:
        print("❌ Invalid email format!")
        return

    contacts[name] = {"phones": phones, "email": email}
    save_contacts()
    print(f"✅ Contact '{name}' added successfully!")

# Show all contacts
def view_contacts():
    if not contacts:
        print("📭 Phonebook is empty.")
        return
    for name, info in contacts.items():
        phone_list = ", ".join([f"{label}: {num}" for label, num in info["phones"].items()])
        print(f"Name: {name}, Phones: [{phone_list}], Email: {info['email']}")

# Search contact by name
def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        phone_list = ", ".join([f"{label}: {num}" for label, num in info["phones"].items()])
        print(f"🔎 Found: Name: {name}, Phones: [{phone_list}], Email: {info['email']}")
    else:
        print(f"❌ No contact found with name '{name}'.")

# Search contact by phone number
def search_by_phone():
    phone = input("Enter phone number to search: ").strip()
    found = False

    for name, info in contacts.items():
        for label, num in info["phones"].items():
            if num == phone:
                print(f"🔎 Found: Name: {name}, Label: {label}, Phone: {num}, Email: {info['email']}")
                found = True

    if not found:
        print(f"❌ No contact found with phone number '{phone}'.")

    

# Update contact details
def update_contact():
    name = input("Enter name to update: ").strip()
    if name in contacts:
        info = contacts[name]

        print("Updating phones...")
        while True:
            print("Current phones:", info["phones"])
            action = input("Choose: [a]dd phone, [u]pdate phone, [d]elete phone, [q]uit: ").strip().lower()

            if action == "a":
                label = input("Enter label for new phone: ").strip().lower()
                phone = input(f"Enter {label} phone number: ").strip()
                if phone.isdigit():
                    info["phones"][label] = phone
                else:
                    print("❌ Invalid number.")

            elif action == "u":
                label = input("Which phone label to update? ").strip().lower()
                if label in info["phones"]:
                    phone = input("Enter new number: ").strip()
                    if phone.isdigit():
                        info["phones"][label] = phone
                    else:
                        print("❌ Invalid number.")
                else:
                    print("❌ No such label.")

            elif action == "d":
                label = input("Which phone label to delete? ").strip().lower()
                if label in info["phones"]:
                    del info["phones"][label]
                else:
                    print("❌ No such label.")

            elif action == "q":
                break

        email = input("Enter new email (leave blank to keep current): ").strip()
        if email:
            if "@" not in email:
                print("❌ Invalid email format!")
                return
            info["email"] = email

        save_contacts()
        print(f"✅ Contact '{name}' updated successfully!")
    else:
        print(f"❌ No contact found with name '{name}'.")
    
    if not info["phones"]:
        print("⚠️ Contact has no phone numbers left!")
        choice = input("Do you want to delete this contact? (y/n): ").strip().lower()
        if choice == "y":
            del contacts[name]
            save_contacts()
            print(f"🗑️ Contact '{name}' deleted because it had no numbers.")


# Delete a contact
def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"🗑️ Contact '{name}' deleted successfully!")
    else:
        print(f"❌ No contact found with name '{name}'.")

# Main menu loop
def main():
    while True:
        print("\n--- 📒 Phonebook Menu ---")
        print("1. Add New Contact")
        print("2. View Contacts")
        print("3. Search Contact by Name")
        print("4. Search Contact by Phone number")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice=="4":
            search_by_phone()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            print("👋 Exiting Phonebook. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
