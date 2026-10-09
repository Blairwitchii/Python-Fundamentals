""" def calculate_tip(bill, percent):
    tip = bill * (percent / 100)
    return tip


bill_amount = float(input("What is your bill "))
tip_percent = float(input("What percent do you want to tip?  "))

tip = calculate_tip(bill_amount, tip_percent)
total = bill_amount + tip

print(f"Tip amount: ${tip}")
print(f"Total to pay: ${total}") """


# Another Version

def calculate_tip(bill_amount, tip_percentage):
    # Calculate tip amount based on bill and tip percentage.

    return bill_amount * (tip_percentage / 100)


# Get user input
bill = float(input("What is your bill? "))
percent = float(input("What percent do you want to tip? "))

# Calculate values
tip_total = calculate_tip(bill, percent)
grand_total = bill + tip_total

# Display results neatly
print(f"Tip amount: ${tip_total:.2f}")
print(f"Total to pay: ${grand_total:.2f}")
