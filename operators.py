# Aritmetic Operators

# Add, Subtract, Multiply, Divide, Modulus, Exponentiation, Floor Division
# +,-,*,/,%,**,//

x = 10
y = 3

print(x+y)  # Addition          10+3 = 13
print(x-y)  # Subtraction       10-3 = 7
print(x*y)  # Multiplication    10*3 = 30
print(x/y)  # Division          10/3 = 3.333...
print(x % y)  # Modulus          10%3 = 1
print(x**y)  # Exponentiation    10**3 = 1000
print(x//y)  # Floor Division    10//3 = 3

# Comparison Operators
print(x == y)  # Equal             10 == 3 = False
print(x != y)  # Not Equal         10 != 3 = True
print(x > y)   # Greater Than      10 > 3 = True
print(x < y)   # Less Than         10 < 3 = False
print(x >= y)  # Greater Than Or Equal 10 >= 3 = True
print(x <= y)  # Less Than Or Equal    10 <= 3 = False

# Logical Operators
# and, or, not

a, b = True, False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# Assignment Operators
# =, +=, -=, *=, /=, %=, **=, //=

x = 5
x += 3  # x = x + 3
x *= 2  # x = x * 2
x /= 4  # x = x / 4
x -= 1  # x = x - 1
print(x)  # 8

# Membership Operators
# in, not in

nums = [1, 2, 3, 4, 5]
print(3 in nums)  # True
print(6 not in nums)  # True

# Identity Operators
# is, is not

x = [1, 2, 3]
y = x

print(x is y)  # True
print(x is not y)  # False

# Bitwise Operators
# &, |, ^, ~, <<, >>

x = 5  # 0101
y = 3  # 0011
print(x & y)  # Bitwise AND     0101 & 0011 = 0001 = 1
print(x | y)  # Bitwise OR      0101 | 0011 = 0111 = 7
print(x ^ y)  # Bitwise XOR     0101 ^ 0011 = 0110 = 6
print(~x)     # Bitwise NOT     ~0101 = 1010 = -6
print(x << 1)  # Left Shift      0101 << 1 = 1010 = 10
print(x >> 1)  # Right Shift     0101 >> 1 = 0010 = 2

# Greater than, Less than, Equal to, Not equal to, Greater than or equal to, Less than or equal to

x = 10
y = 5
print(x > y)   # Greater Than      10 > 5 = True
print(x < y)   # Less Than         10 < 5 = False
print(x == y)  # Equal             10 == 5 = False
print(x != y)  # Not Equal         10 != 5 = True
print(x >= y)  # Greater Than Or Equal 10 >= 5 = True
print(x <= y)  # Less Than Or Equal    10 <= 5 = False

# Keywords: and, or, not, is, in, not in

x = 10
y = 5
print(x and y)  # True
print(x or y)   # True
print(not x)    # False
print(x is y)  # False
print(x in [1, 2, 3, 4, 5])  # True
print(x not in [1, 2, 3, 4, 5])  # False
