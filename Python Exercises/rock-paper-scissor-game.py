import random


def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


"""
choices = get_choices()
print(choices) """

# Longer Version
""" def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")  # Concatenate
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You Win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You Win!"
        else:
            return "Scissors cut paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You Win!"
        else:
            return "Rock smashes scissors! You lose." """

# Cleaner Nested Style


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")

    if player == computer:
        return "It's a tie!"

    # Rock cases
    if player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You Win!"
        else:
            return "Paper covers rock! You lose."

    # Paper cases
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You Win!"
        else:
            return "Scissors cut paper! You lose."

    # Scissors cases
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You Win!"
        else:
            return "Rock smashes scissors! You lose."

# No Messy Elif


""" def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")

    # Dictionary: key = choice, value = what it beats
    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if player == computer:
        return "It's a tie!"

    # Check: does player's choice beat computer's choice?
    if beats[player] == computer:
        return f"{player.capitalize()} smashes {computer}! You Win!"
    else:
        return f"{computer.capitalize()} beats {player}! You lose." """

# Tupple Comparison


""" def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")

    # Dictionary: key = choice, value = what it beats
    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if player == computer:
        return "It's a tie!"

    # Check: does player's choice beat computer's choice?
    if beats[player] == computer:
        return f"{player.capitalize()} beats {computer}! You Win!"
    else:
        return f"{computer.capitalize()} beats {player}! You lose." """


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
