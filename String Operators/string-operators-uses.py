# ==================================================
# 1️⃣ STRING CONCATENATION (+) → Combine pieces into one
# ==================================================
first_name = "Maria"
last_name = "Santos"
full_name = first_name + " " + last_name  # joins with space
print("Full Name:", full_name)
# Output: Full Name: Maria Santos

# ==================================================
# 2️⃣ STRING REPETITION (*) → Create banners, lines, separators
# ==================================================
divider = "=" * 35  # repeat character N times
print(divider)
# Output: ===================================

# ==================================================
# 3️⃣ STRING COMPARISON (==, !=, <, >) → Sorting & validation
# Compares alphabetically using Unicode values (a=97, b=98... z=122)
# ==================================================
member_tier1 = "Gold"
member_tier2 = "Silver"

print("Tier equal?", member_tier1 == member_tier2)   # False
print("Tier different?", member_tier1 != member_tier2)  # True
print("Gold comes BEFORE Silver?", member_tier1 < member_tier2)
# True → because 'G'(71) < 'S'(83) in Unicode

# ==================================================
# 4️⃣ MEMBERSHIP (in / not in) → Search & check existence
# ==================================================
active_members = "Maria Santos | John Doe | Anna Cruz"
print("Is Maria active?", "Maria Santos" in active_members)     # True
print("Is Mark active?", "Mark" in active_members)               # False
print("Mark is NOT active?", "Mark" not in active_members)       # True

# ==================================================
# 5️⃣ SLICING [start:end] → Extract parts: initials, short names, codes
# ==================================================
# Get first name initial → index 0
first_initial = full_name[0]
# Get last name initial → at index after the space (index 6)
last_initial = full_name[6]

print("First Initial:", first_initial)   # M
print("Last Initial:", last_initial)     # S

# Extract first 5 characters
short_code = full_name[0:5]
print("Short Code:", short_code)         # Maria
print(divider)  # Output: ===================================
