# Dictionary

# Syntax
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

mydict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(mydict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# dictionary operations
print(mydict["name"])  # Output: Alice
print(mydict["age"])   # Output: 30
print(mydict["city"])  # Output: New York

# add a new key-value pair
mydict["country"] = "USA"
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}
print(mydict)

# remove a key-value pair
del mydict["age"]
# Output: {'name': 'Alice', 'city': 'New York', 'country': 'USA'}
print(mydict)

# REplace a value for an existing key
mydict["city"] = "Los Angeles"
# Output: {'name': 'Alice', 'city': 'Los Angeles', 'country': 'USA'}
print(mydict)
