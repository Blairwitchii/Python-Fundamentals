# Arithmetic Operators → Daily Budget & Shopping

budget = 5000
spent = 1200
weeks = 4

# +  → Total if you add extra allowance
total_with_bonus = budget + 500   # 5500

# -  → Remaining money after spending
remaining = budget - spent         # 3800

# *  → Cost if you bought this same amount every month
yearly_cost = spent * 12           # 14400

# /  → Exact amount available per week
per_week_exact = remaining / weeks  # 950.0

# %  → What's left AFTER splitting evenly (remainder)
leftover = remaining % weeks       # 0 — perfectly divides

# ** → If your budget grew 10% every month for 6 months
growth = budget * (1.10 ** 6)      # ~8857.81

# // → Whole pesos per week (no decimals)
per_week_whole = remaining // weeks  # 950

print(f"Bonus budget: ₱{total_with_bonus}")
print(f"Remaining: ₱{remaining}")
print(f"Per week (exact): ₱{per_week_exact}")
print(f"Per week (whole): ₱{per_week_whole}")
print(f"Leftover pesos: ₱{leftover}")
print(f"Budget after 6 months growth: ₱{growth:.2f}")


# ✅ Key takeaway:
# / = precise math (prices, averages)
# // = whole units only (people, bottles, full weeks)
# % = “what’s left over after sharing equally”
# ** = compound growth / interest
