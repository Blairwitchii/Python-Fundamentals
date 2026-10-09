full_dot = '●'
empty_dot = '○'


def create_character(character_name, *args, **kwargs):
    if not isinstance(character_name, str):
        return "The character name should be a string"
    if character_name == "":
        return "The character should have a name"
    if len(character_name) > 10:
        return "The character name is too long"
    if " " in character_name:
        return "The character name should not contain spaces"

    for stat in args:
        if not isinstance(stat, int) or isinstance(stat, bool):
            return "All stats should be integers"
    for stat in args:
        if stat < 1:
            return "All stats should be no less than 1"

    for stat in args:
        if stat > 4:
            return "All stats should be no more than 4"
    if sum(args) != 7:
        return "The character should start with 7 points"

    str_val, int_val, cha_val = args
    str_bar = full_dot * str_val + empty_dot * (10 - str_val)
    int_bar = full_dot * int_val + empty_dot * (10 - int_val)
    cha_bar = full_dot * cha_val + empty_dot * (10 - cha_val)

    return f"""{character_name}
STR {str_bar}
INT {int_bar}
CHA {cha_bar}"""
