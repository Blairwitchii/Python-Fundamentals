# Logical Operators → Eligibility Check

age = 22
has_membership = True
is_vip = False

# and → BOTH conditions must be True
can_join = (age >= 18) and has_membership   # True ✅

# or → EITHER can be True
special_access = is_vip or (age >= 60)      # False

# not → Flip True ↔ False
needs_renewal = not has_membership          # False (still valid)

print(f"Can join: {can_join}")
print(f"Special access: {special_access}")
print(f"Needs renewal: {needs_renewal}")
