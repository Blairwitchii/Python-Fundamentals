my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Output: (1, 2, 3, 4, 5)


# tuple operations

# access tuple elements using index
print(my_tuple[0])  # Output: 1

# no append or remove methods for tuples, as they are immutable

# concatenation of tuples is possible
tuple_2 = (6, 7, 8)
new_tuple = my_tuple + tuple_2
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)

# Build Sequences Dynamically
part1 = (10, 20)
part2 = (30, 40)
part3 = (50,)  # ← comma required for single-element tuple
full = part1 + part2 + part3
print(full)  # Output: (10, 20, 30, 40, 50)
# Result: (10, 20, 30, 40, 50)

# Return Multiple Values Together


def get_user_data():
    ids = (101, 102)
    names = ("Alice", "Bob")
    return ids + names  # Combine into one tuple


result = get_user_data()
print(result)
# Output: (101, 102, 'Alice', 'Bob')


# Your home location — fixed, should never be altered
home_location = (15.05, 120.65)   # (latitude, longitude)

# Two places you visit often
work_location = (14.60, 120.98)
cafe_location = (15.03, 120.64)

# Combine into a list of places
all_places = home_location, work_location, cafe_location

print("📍 Saved Locations:")
print(all_places)

""" Use tuples whenever your data is:
✔️ Fixed / constant
✔️ Order matters
✔️ Should NOT be changed by accident
✔️ Simple grouping of related items
Use lists when you need to add, remove, or change items later. """
