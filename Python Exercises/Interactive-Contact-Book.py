# ======================================================
# 📒 INTERACTIVE CONTACT BOOK
# ======================================================

# Start with an empty contact book
contacts = {}


def show_menu():
    print("\n" + "="*35)
    print("   📒 CONTACT BOOK — MAIN MENU")
    print("="*35)
    print(" 1️⃣  Add a new contact")
    print(" 2️⃣  View a contact's number")
    print(" 3️⃣  Update a contact's number")
    print(" 4️⃣  Delete a contact")
    print(" 5️⃣  Show ALL contacts")
    print(" 0️⃣  Exit")
    print("-"*35)


# --- MAIN PROGRAM LOOP ---
while True:
    show_menu()
    choice = input("👉 Enter your choice (0-5): ").strip()

    # ✅ 0. Exit
    if choice == "0":
        print("\n👋 Goodbye! Closing Contact Book...")
        break

    # ✅ 1. Add Contact
    elif choice == "1":
        name = (input("✏️ Enter contact NAME: ").strip().title())
        if not name:
            print("❌ Name cannot be empty!")
            continue
    # Strict check: must NOT be all digits; must contain only letters/spaces
        if name.replace(" ", "").isdecimal():
            print("❌ Name cannot be a number! Use letters only.")
            continue
        if not all(c.isalpha() or c.isspace() for c in name):
            print("❌ Name can only contain letters and spaces! No numbers or symbols.")
            continue
        if name in contacts:
            print(f"⚠️ '{name}' already exists! Use Update instead.")
            continue
        phone_input = input("📞 Enter PHONE NUMBER: ").strip()
        if not phone_input:
            print("❌ Number cannot be empty!")
            continue
        if not phone_input.isdigit():
            print("❌ Invalid number! Enter DIGITS ONLY — no spaces, letters, or symbols.")
            continue

        number = int(phone_input)
        contacts[name] = number
        print(f"✅ Added: {name} → {number}")

    # ✅ 2. View Contact
    elif choice == "2":
        name = input("🔍 Enter NAME to look up: ").strip().title()
        if name in contacts:
            print(f"📞 {name}: {contacts[name]}")
        else:
            print(f"❌ Contact '{name}' NOT found!")

    # ✅ 3. Update Contact
    elif choice == "3":
        name = input("✏️ Enter NAME to update: ").strip().title()
        if name not in contacts:
            print(f"❌ Contact '{name}' NOT found!")
            continue
        new_number = input(f"📞 Enter NEW number for {name}: ").strip()
        if not new_number:
            print("❌ Number cannot be empty!")
            continue
        contacts[name] = new_number
        print(f"✅ Updated: {name} → {contacts[name]}")

    # ✅ 4. Delete Contact
    elif choice == "4":
        name = input("🗑️ Enter NAME to delete: ").strip().title()
        if name in contacts:
            del contacts[name]
            print(f"🗑️ Deleted '{name}' successfully!")
        else:
            print(f"❌ Contact '{name}' NOT found!")

    # ✅ 5. Show All
    elif choice == "5":
        if not contacts:
            print("📭 Your contact book is EMPTY!")
        else:
            print("\n" + "📋 ALL CONTACTS:")
            print("-"*30)
            for name, number in contacts.items():
                print(f" {name:<20} → {number}")
            print("-"*30)

    # ❌ Invalid choice
    else:
        print("⚠️ Invalid choice! Please enter a number 0–5.")
5
