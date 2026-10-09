full_dot = '●'
empty_dot = '○'


def create_character(character_name, *args, **kwargs):
    # ── Name validation ──────────────────────────────
    if not isinstance(character_name, str):
        return "The character name should be a string"
    if character_name == "":
        return "The character should have a name"
    if len(character_name) > 10:
        return "The character name is too long"
    if " " in character_name:
        return "The character name should not contain spaces"

    # ── Rule 11: All stats must be integers ───────────
    for stat in args:
        if not isinstance(stat, int) or isinstance(stat, bool):
            return "All stats should be integers"

    # ── Rule 12: Min value = 1 ───────────────────────
    for stat in args:
        if stat < 1:
            return "All stats should be no less than 1"

    # ── Rule 14: Max value = 4 ───────────────────────
    for stat in args:
        if stat > 4:
            return "All stats should be no more than 4"

    # ── Rule 16: Sum must equal 7 ─────────────────────
    if sum(args) != 7:
        return "The character should start with 7 points"

    # ── Rule 18 & 19: Build formatted output ──────────
    str_val, int_val, cha_val = args
    str_bar = full_dot * str_val + empty_dot * (10 - str_val)
    int_bar = full_dot * int_val + empty_dot * (10 - int_val)
    cha_bar = full_dot * cha_val + empty_dot * (10 - cha_val)

    return f"""{character_name}
STR {str_bar}
INT {int_bar}
CHA {cha_bar}"""


# ═══════════════════════════════════════════════════════
# 🧪 TEST CASES — Run these to see EVERY rule in action
# ═══════════════════════════════════════════════════════

print("=" * 50)
print("✅ TEST 1: Valid values — create_character('ren', 4, 2, 1)")
print("-" * 50)
result = create_character('ren', 4, 2, 1)
print(result)
print()

print("=" * 50)
print("❌ TEST 2: Non-integer stat → should return integer error")
print("-" * 50)
print(create_character('Mage', 3, 'two', 2))
print()

print("=" * 50)
print("❌ TEST 3: Stat below 1 → should return min error")
print("-" * 50)
print(create_character('Rogue', 0, 4, 3))
print()

print("=" * 50)
print("❌ TEST 4: Stat above 4 → should return max error")
print("-" * 50)
print(create_character('Knight', 5, 1, 1))
print()

print("=" * 50)
print("❌ TEST 5: Sum not 7 → should return sum error")
print("-" * 50)
print(create_character('Healer', 2, 2, 2))
print()

print("=" * 50)
print("✅ TEST 6: Another valid character")
print("-" * 50)
print(create_character('Hero', 1, 3, 3))
