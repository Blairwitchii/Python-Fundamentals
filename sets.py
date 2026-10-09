# Sets

my_set = {1, 2, 3, 4, 5}
print(my_set)

# Add an element to the set
my_set.add(6)
print(my_set)

# remove an element from the set
my_set.remove(3)
print(my_set)

# union, intersection and difference of sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)

# Create & Modify SetsCreate & Modify Sets
latte_buyers = {"Alice", "Bob", "Charlie", "Diana"}
cappuccino_buyers = {"Charlie", "Diana", "Eve", "Frank"}

# New customer "Grace" just bought a latte → ADD
latte_buyers.add("Grace")
print(latte_buyers)
# Output: {'Alice', 'Bob', 'Charlie', 'Diana', 'Grace'}

# "Bob" cancelled his order → REMOVE
latte_buyers.remove("Bob")
print(latte_buyers)
# Output: {'Alice', 'Charlie', 'Diana', 'Grace'}

# UNION → All Customers (Latte OR Cappuccino)
all_customers = latte_buyers | cappuccino_buyers
print("All customers who bought anything:", all_customers)
# Output: {'Alice', 'Charlie', 'Diana', 'Grace', 'Eve', 'Frank'}

# DIFFERENCE → Bought Latte ONLY (NOT Cappuccino)
latte_only = latte_buyers - cappuccino_buyers
print("Bought ONLY latte:", latte_only)
# Output: {'Alice', 'Grace'}
