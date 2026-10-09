# ======================================================
# ☕ COFFEE SHOP — FULL SET OPERATIONS DEMO
# ======================================================

# --------------------------
# Step 1: Create our sets
# --------------------------
# Set A: Customers who bought a Latte
latte_buyers = {"Alice", "Bob", "Charlie", "Diana"}
# Set B: Customers who bought a Cappuccino
cappuccino_buyers = {"Charlie", "Diana", "Eve", "Frank"}

print("=" * 50)
print("=== INITIAL CUSTOMER LISTS ===")
print("Latte buyers:      ", latte_buyers)
print("Cappuccino buyers: ", cappuccino_buyers)
print("=" * 50)
print()

# --------------------------
# Step 2: Add & Remove Customers
# --------------------------
print("=== ADDING & REMOVING ITEMS ===")

# Add a new customer who just ordered a Latte
latte_buyers.add("Grace")
print("✅ After adding 'Grace' to Latte list:")
print("   ", latte_buyers)

# --- .remove() vs .discard() ---
# .remove(x) → removes x; raises ERROR if x is NOT found
# .discard(x) → removes x; does NOT raise error if missing

# Remove Bob — we know he's in the list → safe to use .remove()
latte_buyers.remove("Bob")
print("✅ After removing 'Bob':")
print("   ", latte_buyers)

# Try to remove someone who IS NOT in the list
# latte_buyers.remove("Zack")  # ❌ This would CRASH the program!
latte_buyers.discard("Zack")  # ✅ Safe — does nothing, NO error
print("✅ Tried to remove 'Zack' (not in list) using .discard() → No error!")
print()

# --------------------------
# Step 3: All Set Operations
# --------------------------
print("=" * 50)
print("=== SET OPERATIONS RESULTS ===")
print("=" * 50)

# UNION → ALL customers who bought ANY drink (no duplicates)
# Symbol: |   or method: .union()
all_customers = latte_buyers | cappuccino_buyers
# all_customers = latte_buyers.union(cappuccino_buyers)  # alternative way
print("1️⃣  UNION (Everyone who bought ANYTHING):")
print("   ", all_customers)
print()

# INTERSECTION → Customers who bought BOTH drinks
# Symbol: &   or method: .intersection()
both_drinks = latte_buyers & cappuccino_buyers
# both_drinks = latte_buyers.intersection(cappuccino_buyers)  # alternative way
print("2️⃣  INTERSECTION (Bought BOTH Latte AND Cappuccino):")
print("   ", both_drinks)
print()

# DIFFERENCE → Latte buyers who DID NOT buy Cappuccino
# Symbol: -   or method: .difference()
latte_only = latte_buyers - cappuccino_buyers
# latte_only = latte_buyers.difference(cappuccino_buyers)  # alternative way
print("3️⃣  DIFFERENCE (Latte ONLY — no Cappuccino):")
print("   ", latte_only)
print()

# SYMMETRIC DIFFERENCE → bought ONE drink OR THE OTHER, BUT NOT BOTH
# Symbol: ^   or method: .symmetric_difference()
one_drink_only = latte_buyers ^ cappuccino_buyers
# one_drink_only = latte_buyers.symmetric_difference(cappuccino_buyers)  # alternative way
print("4️⃣  SYMMETRIC DIFFERENCE (Bought ONE drink ONLY — NOT both):")
print("   ", one_drink_only)
print()

# --------------------------
# Quick Reference Summary
# --------------------------
print("=" * 50)
print("📋 QUICK CHEAT SHEET")
print("=" * 50)
print("Union       |  A | B        → All items in A OR B")
print("Intersection|  A & B        → Items in BOTH A and B")
print("Difference  |  A - B        → Items in A but NOT in B")
print("Sym Diff    |  A ^ B        → Items in A or B but NOT both")
print(".remove(x)  |               → Delete x → ERROR if not found!")
print(".discard(x) |               → Delete x → No error if not found")
print("=" * 50)
