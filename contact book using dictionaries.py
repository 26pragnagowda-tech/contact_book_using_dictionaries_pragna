# Contact Book Using Dictionaries

contacts = {}


def add_contact():
    print("\n--- Add Contact ---")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone:
        print("Name and phone number cannot be empty.")
        return

    if phone in contacts:
        print("Error: This phone number already exists!")
        return

    contacts[phone] = {
        "name": name,
        "email": email
    }

    print("Contact added successfully!")


def search_contact():
    print("\n--- Search Contact ---")
    search = input("Enter name or phone number: ").strip().lower()

    found = False

    for phone, details in contacts.items():
        if (search == phone.lower()
                or search in details["name"].lower()):
            print("\nContact Found")
            print("Name:", details["name"])
            print("Phone:", phone)
            print("Email:", details["email"])
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    print("\n--- Update Contact ---")
    phone = input("Enter the phone number of the contact: ").strip()

    if phone not in contacts:
        print("Contact not found.")
        return

    print("Leave a field blank to keep its current value.")

    name = input("Enter new name: ").strip()
    new_phone = input("Enter new phone number: ").strip()
    email = input("Enter new email: ").strip()

    if new_phone and new_phone != phone and new_phone in contacts:
        print("Error: This phone number already exists!")
        return

    updated_name = name if name else contacts[phone]["name"]
    updated_email = email if email else contacts[phone]["email"]
    updated_phone = new_phone if new_phone else phone

    contacts[updated_phone] = {
        "name": updated_name,
        "email": updated_email
    }

    if updated_phone != phone:
        del contacts[phone]

    print("Contact updated successfully!")


def delete_contact():
    print("\n--- Delete Contact ---")
    phone = input("Enter the phone number to delete: ").strip()

    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def view_contacts():
    print("\n--- All Contacts ---")

    if not contacts:
        print("No contacts available.")
        return

    for phone, details in contacts.items():
        print("--------------------")
        print("Name:", details["name"])
        print("Phone:", phone)
        print("Email:", details["email"])


def main():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            view_contacts()
        elif choice == "6":
            print("Thank you for using Contact Book!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
