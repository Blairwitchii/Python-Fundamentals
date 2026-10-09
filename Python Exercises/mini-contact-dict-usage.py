# ==============================================
# MINI CONTACT BOOK
# ==============================================

# 📌 1. CREATE: Start with some contacts
contacts = {
    "Alice": "555-0101",
    "Bob": "555-0102",
    "Charlie": "555-0103"
}

print("📖 === MY CONTACT BOOK ===")
print("All contacts:", contacts)
print()

# 🔍 2. READ: Look up a contact's number
print("🔍 Alice's number:", contacts["Alice"])
print("🔍 Bob's number:", contacts["Bob"])
print()

# ➕ 3. ADD: Add a new contact
contacts["Diana"] = "555-0104"
contacts["Eve"] = "555-0105"
print("✅ After adding Diana & Eve:")
print(contacts)
print()

# ✏️ 4. UPDATE: Change an existing number
contacts["Alice"] = "555-9999"
print("✏️ After updating Alice's number:")
print("Alice's NEW number:", contacts["Alice"])
print()

# ➖ 5. DELETE: Remove a contact
del contacts["Charlie"]
print("🗑️ After removing Charlie:")
print(contacts)
print()

# 🎁 BONUS: Loop through ALL contacts nicely
print("📋 Full Contact List:")
for name, number in contacts.items():
    print(f"   {name}: {number}")
