# Identity Operators → Same Item or Copy?
# Scenario: Two shopping carts — are they literally the same cart, or just contain the same things?

cart_a = ["apples", "bananas"]
cart_b = cart_a               # ← SAME cart (two names, one thing)
cart_c = ["apples", "bananas"]  # ← Separate cart, same contents

print(cart_b is cart_a)        # True → SAME object
print(cart_c is cart_a)        # False → Different objects
print(cart_c == cart_a)        # True → Same contents though!


# ✅ Key takeaway:
# is → Are they the exact same thing in memory?
# == → Do they have the same value?
# Use is for None / True / False checks; use == for comparing values
