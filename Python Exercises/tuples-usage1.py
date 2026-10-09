# These are fixed — order matters, won't change
weekday_dinners = ("Adobo", "Sinigang", "Lechon Kawali",
                   "Tinola", "Chicken Inasal")
weekend_dinners = ("Pancit Palabok", "Seafood Kare-Kare")

# Combine them to make the FULL week plan
full_week_plan = weekday_dinners + weekend_dinners

print("📅 Full Weekly Dinner Plan:")
for day, meal in enumerate(full_week_plan, start=1):
    print(f"Day {day}: {meal}")
