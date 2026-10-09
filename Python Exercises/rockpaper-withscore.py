import random


def check_win(player, computer):
    print(f"\nYou chose {player}, computer chose {computer}")

    beats = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if player == computer:
        return "tie"
    elif beats[player] == computer:
        return "win"
    else:
        return "lose"


# --- MAIN GAME WITH SCORE (FIRST TO 5) ---
print("🏆 ROCK PAPER SCISSORS — FIRST TO 5 WINS! 🏆")

while True:
    # Reset scores for a new match
    player_score = 0
    computer_score = 0
    target = 5

    while player_score < target and computer_score < target:
        print(f"\n📊 SCORE — You: {player_score} | Computer: {computer_score}")
        print("--- New Round ---")

        # Get player choice
        player_choice = input(
            "Choose rock/paper/scissors (or 'q' to quit): ").lower()

        if player_choice in ["q", "quit"]:
            print("\nThanks for playing! 👋")
            exit()  # Stop everything

        if player_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice! Try again.")
            continue

        # Computer choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Get result
        result = check_win(player_choice, computer_choice)

        # Update score & show message
        if result == "tie":
            print("⚖️ It's a tie! No points.")
        elif result == "win":
            player_score += 1
            print(f"✅ You Win this round! +1 point")
        else:
            computer_score += 1
            print(f"❌ You Lose this round! Computer +1 point")

    # --- Match Over ---
    print("\n" + "="*40)
    if player_score == target:
        print(f"🎉 CONGRATULATIONS! YOU WON THE MATCH!")
    else:
        print(f"😔 Computer won the match this time!")
    print(f"FINAL SCORE — You: {player_score} | Computer: {computer_score}")
    print("="*40)

    # Play another match?
    play_again = input("\nPlay another match? (y/n): ").lower()
    if play_again not in ["y", "yes"]:
        print("Thanks for playing! 👋")
        break
