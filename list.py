# List

my_list = [1, 2, 3, 4, 5, "red", "blue", "green"]
print(my_list)  # Output: [1, 2, 3, 4, 5, 'red', 'blue', 'green']

# list operations
# access list elements using index
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 'green'
print(my_list[2:5])  # Output: [3, 4, 5]
print(my_list[5:8])  # Output: ['red', 'blue', 'green']


# append an item to the end of the list
my_list.append("yellow")
print(my_list)  # Output: [1, 2, 3, 4, 5, 'red', 'blue', 'green', 'yellow']

# remove an item from the list
my_list.remove("blue")
print(my_list)  # Output: [1, 2, 3, 4, 5, 'red', 'green', 'yellow']

# replace an item in the list
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5, 'red', 'green', 'yellow']


# Real-World Example Putting It All Together
tasks = ["buy milk", "finish report", "call mom"]

# Access first task
print("First:", tasks[0])           # → buy milk

# Get last two tasks
print("Remaining:", tasks[1:3])     # → ['finish report', 'call mom']

# Add new task
tasks.append("pay bills")

# Remove completed task
tasks.remove("buy milk")

# Rename/edit a task
tasks[0] = "finish project report"

print(tasks)
# → ['finish project report', 'call mom', 'pay bills']
