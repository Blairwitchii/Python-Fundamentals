#  Bitwise Operators → Settings & Permissions (Advanced)

# Permission flags (each is a power of 2)
READ = 1    # 0001
WRITE = 2   # 0010
EDIT = 4    # 0100

# Give READ + WRITE permission
my_perms = READ | WRITE     # 0011 = 3

# Check if they have EDIT permission
can_edit = (my_perms & EDIT) != 0  # False

# Add EDIT permission
my_perms = my_perms | EDIT          # Now 0111 = 7

print(f"Permissions code: {my_perms}")
print(
    f"Can edit now? {can_edit} → Actually can edit: {(my_perms & EDIT) != 0}")


# ✅ Key takeaway: Bitwise is rare for everyday use — but super fast for toggling ON/OFF switches, flags, and permissions.
