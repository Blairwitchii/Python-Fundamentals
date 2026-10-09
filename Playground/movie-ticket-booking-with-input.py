base_price = 15
age = 0
seat_type = ''
show_time = ''

age = int(input("Please enter your age: "))

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
    show_time = input("Please enter the show time (Day/Evening): ")
else:
    print('User is not eligible for Evening shows')

is_member = ''
is_weekend = False

is_member = input("Are you a member? (yes/no): ").strip().lower() == 'yes'

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
    seat_type = input("Please enter your seat type (Premium/Gold): ")

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    final_price = base_price + extra_charges + service_charges - discount
    print('Final price of ticket:', final_price)

else:
    print('Ticket booking failed due to restrictions')
