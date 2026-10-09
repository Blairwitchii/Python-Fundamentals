# Membership Operators → Check Your Shopping List

shopping_list = ["oats", "honey", "green tea", "vitamins"]

bought = "green tea"
missing = "protein powder"

print(bought in shopping_list)       # True ✔️ on list
print(missing not in shopping_list)  # True ❌ not listed
print("oats" in shopping_list)         # True ✔️ on list
print(missing)


# ✅ Key takeaway:
# in → “Is this item INSIDE the group?”
# not in → “Is this NOT inside?”
# Works great with lists, text, dictionaries
