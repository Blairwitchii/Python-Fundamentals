#  Comparison Operators → Health & Fitness Goals

my_steps = 200
goal = 8000

print(my_steps == goal)   # Equal?           → False (did more!)
print(my_steps != goal)   # Not equal?       → True
print(my_steps > goal)    # Above goal?       → True
print(my_steps < goal)    # Below goal?       → False
print(my_steps >= goal)   # Met or above?     → True ✅
print(my_steps <= goal)   # At or below?      → False


def check_steps(steps, goal):
    if steps >= goal:
        return "Great job!"
    else:
        return "Keep going!"


print(check_steps(my_steps, goal))  # Output: Great job!
