name = "Alice"  # string
age = 25  # integer
height = 5.6  # float
is_student = True  # boolean


print(f"My name is {name}, I'm {age} years old, my height is {height} feet, and it is {is_student} that I am a student.")


# Print the values
print(name)
print(age)
print(height)
print(is_student)

# Print the data types
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


a = b = c = 10
print(a, b, c)  # Output: 10 10 10
# Output: <class 'int'> <class 'int'> <class 'int'>
print(type(a), type(b), type(c))
print(a)
print(b)
print(c)

a, b = 5, 10
print(a)  # Output: 5
print(b)  # Output: 10

a, b = b, a  # Swap values
print(a)  # Output: 10
print(b)  # Output: 5

x = 5
y = "5"
print(x + int(y))  # Output: 10
