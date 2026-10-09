# ==============================================
# 🛒 INTERACTIVE SHOPPING CART — insert() & pop()
# ==============================================

print("🛒 WELCOME TO YOUR SHOPPING CART!")
print("Commands:")
print("  add POSITION ITEM   → e.g. add 1 Butter")
print("  remove POSITION      → e.g. remove 2")
print("  remove-last          → remove last item")
print("  show                 → see your cart")
print("  quit                 → exit\n")

# Start with an empty cart
cart = []

while True:
    # Show current cart with indices every time
    print("-" * 50)
    print("📦 Your cart now:", cart)
    # Show positions clearly
    if cart:
        print("🔢 Positions:   ", "  ".join(str(i) for i in range(len(cart))))
    print("-" * 50)

    # Get your command
    cmd = input("Enter command ➜ ").strip()
    if not cmd:
        continue

    parts = cmd.split()
    action = parts[0].lower()

    # ✅ ADD: insert at exact position
    if action == "add":
        if len(parts) < 3:
            print("⚠️  Use: add POSITION ITEM  (example: add 1 Butter)")
            continue
        try:
            pos = int(parts[1])
            item = " ".join(parts[2:])
            cart.insert(pos, item)
            print(f"✅ ADDED '{item}' at position {pos}")
        except ValueError:
            print("❌ Position must be a NUMBER!")

    # ❌ REMOVE BY POSITION: pop(index)
    elif action == "remove":
        if len(parts) < 2:
            print("⚠️  Use: remove POSITION  (example: remove 2)")
            continue
        try:
            pos = int(parts[1])
            removed = cart.pop(pos)
            print(f"🗑️  REMOVED '{removed}' from position {pos}")
        except IndexError:
            print(f"❌ Position doesn't exist! Cart has {len(cart)} items.")
        except ValueError:
            print("❌ Position must be a NUMBER!")

    # 🧹 REMOVE LAST: pop() with NO index
    elif action == "remove-last":
        if cart:
            removed = cart.pop()
            print(f"🗑️  REMOVED LAST ITEM: '{removed}'")
        else:
            print("📭 Cart is already empty!")

    # 👀 Show cart
    elif action == "show":
        print("📋 Full cart:", cart)

    # 👋 Quit
    elif action == "quit":
        print("👋 Final cart:", cart)
        print("Bye!")
        break

    else:
        print("❌ Unknown command. Try: add / remove / remove-last / show / quit")
