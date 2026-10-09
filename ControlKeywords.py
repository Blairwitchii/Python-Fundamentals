# Break

# Stop the loop immediately

movies = ["Inception", "The Matrix", "Spiderman", "Titanic"]
for movie in movies:
    print("Now watching:", movie)
    if movie == "Spiderman":
        print("Found my favorite movie! stopping the marathon")
        break


# Continue Statement
# Skip remaining in the current iteration

dishes = ["Pasta", "Spicy Curry", "Salad", "Spicy Noodles"]
for dish in dishes:
    if "Spicy" in dish:
        print("skipping:*", dish)
        continue
    print("Eating:", dish)

# Pass
# placeholder for possible future logic

tasks = ["Clean the room", "Skip"]
for task in tasks:
    if task == "Skip":
        pass
    else:
        print("Doing task:", task)
