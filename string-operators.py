# String Concatination

first_name = "John"
last_name = "Doe"

# full_name = first_name + " " + last_name

full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe


# String Repetition (*)

word = "Hello "
# repeated_word = word * 3

repeat_count = 3
repeated_word = word * repeat_count
print(repeated_word)  # Output: HelloHelloHello


# string Comparison or Relational Operators (==, !=, <, >, <=, >=)

fruit1 = "apple"
fruit2 = "banana"

print(fruit1 == fruit2)  # Output: False
print(fruit1 != fruit2)  # Output: True
print(fruit1 < fruit2)   # Output: True
print(fruit1 > fruit2)   # Output: False
print(fruit1 <= fruit2)  # Output: True
print(fruit1 >= fruit2)  # Output: False

# unicode value of a is 97, b is 98, c is 99, d is 100, e is 101, f is 102, g is 103, h is 104, i is 105, j is 106, k is 107, l is 108, m is 109, n is 110, o is 111, p is 112, q is 113, r is 114, s is 115, t is 116, u is 117, v is 118, w is 119, x is 120, y is 121 and z is 122


# String Membership Operators (in, not in)

sentence = "The quick brown fox jumps over the lazy dog"
print("quick" in sentence)  # Output: True
print("elephant" in sentence)  # Output: False
print("quick" not in sentence)  # Output: False
print("elephant" not in sentence)  # Output: True


# string slicing or indexing
text = "Hello, World!"

# Extracting the word Hello from the string text

extracted_word = text[0:5]  # Slicing from index 0 to 4
print(extracted_word)  # Output: Hello


# Program to compute the remainder using the modulus operator

# Taking two numbers as input from the user
num1 = int(input("Enter the first number (dividend): "))
num2 = int(input("Enter the second number (divisor, not 0): "))

# Calculating the remainder
remainder = num1 % num2

# Displaying the result
print("The remainder when", num1, "is divided by ", num2, " is: ", remainder)

# Program to check if a number is greater than, less than, or equal to 10

# Taking a number as input from the user
number = float(input("Enter a number: "))

# Using expressions to check conditions
is_greater = number > 10
is_less = number < 10
is_equal = number == 10

# Displaying the results based on expressions
print("The number is greater than 10:", is_greater)
print("The number is less than 10:", is_less)
print("The number is equal to 10:", is_equal)

# Program to check if a number is between 1 and 100

# Taking a number as input from the user
number = float(input("Enter a number: "))

# Checking if the number is between 1 and 100 using the 'and' operator
is_in_range = number >= 1 and number <= 100

# Displaying the result
print(f"Is the number between 1 and 100? {is_in_range}")

# Program to check if a number is not negative

# Taking a number as input from the user
number = float(input("Enter a number: "))

# Checking if the number is not negative using the 'not' operator
is_not_negative = not (number < 0)

# Displaying the result
print("Is the number not negative?", is_not_negative)


# Program to increase a number by 5 and then multiply it by 2

# Taking a number as input from the user
number = float(input("Enter a number: "))

# Increasing the number by 5 using the += operator
number += 5

# Multiplying the number by 2 using the *= operator
number *= 2

# Displaying the final result
print("The final result is:", number)
