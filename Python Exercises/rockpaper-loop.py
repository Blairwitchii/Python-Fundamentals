import random


def check_win(player, computer):
    print(f"\nYou chose {player}, computer chose {computer}")

    # Dictionary: what beats what
    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if player == computer:
        return "It's a tie!"
    elif beats[player] == computer:
        return f"{player.capitalize()} beats {computer}! ✅ You Win!"
    else:
        return f"{computer.capitalize()} beats {player}! ❌ You lose."


# --- MAIN GAME LOOP ---
while True:
    # Let player choose
    print("\n--- Rock Paper Scissors ---")
    player_choice = input(
        "Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()

    # Exit if player wants to stop
    if player_choice in ["q", "quit"]:
        print("Thanks for playing! 👋")
        break

    # Validate input
    if player_choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice! Please enter rock, paper, or scissors.")
        continue  # Go back to start of loop

    # Computer chooses randomly
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Check & show result
    result = check_win(player_choice, computer_choice)
    print(result)
