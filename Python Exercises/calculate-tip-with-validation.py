# With Input Validation

def calculate_tip(bill_amount, tip_percentage):
    """Calculate tip amount based on bill total and tip percentage."""
    return bill_amount * (tip_percentage / 100)


def get_valid_number(prompt):
    """Prompt user until they enter a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


# Get validated inputs
bill = get_valid_number("What is your bill? $")
percent = get_valid_number("What percentage do you want to tip? ")

# Perform calculations
tip = calculate_tip(bill, percent)
total = bill + tip

# Display neatly formatted results
print(f"\n💵 Tip amount: ${tip:.2f}")
print(f"💰 Total to pay: ${total:.2f}")
