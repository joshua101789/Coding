import random

computer_score = 0
user_score = 0
tie = 0

def score():
    print(f"The score stands: You have {user_score} points, I have {computer_score} points, and we have tied {tie} times.")

while True:
    user_action = input("Enter a choice:(rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_actions = random.choice(possible_actions)

    print(f"\nYou chose {user_action}, I chose {computer_actions}.\n")

    if user_action == computer_actions:
        print(f"Both players selected {user_action}. It's a tie!")
        tie += 1
        score()
    elif user_action == "rock":
        if computer_actions == "scissors":
            print("Rock Smashes Scissors! You Win!")
            user_score += 1
            score()
        else:
            print("Paper covers rock! You Lose.")
            computer_score += 1
            score()
    elif user_action == "paper":
        if computer_actions == "rock":
            print("Paper covers rock! You win!")
            user_score += 1
            score()
        else:
            print("Scissors cuts paper! You loose.")
            computer_score += 1
            score()
    elif user_action == "scissors":
        if computer_actions == "rock":
            print("Rock smashes scissors! You loose.")
            computer_score += 1
            score()
        else:
            print("Scissors cut paper! You win!")
            user_score += 1
            score()
    else:
        print("Please play by the rules!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

