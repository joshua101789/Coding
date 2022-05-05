import random

# 1 = R = Rock
# 2 = P = Paper
# 3 = S = Scissors


# Rock > Scissors
# Paper > Rock
#  Scissors > Paper

#Computer Guess will be number based!

computerScore = 0
personScore = 0
tie = 0

while True:
    computer = random.randint(1, 3)

    person = int(input("Rock{1} Paper{2} or Scissors{3}? "))

    rock = 1
    paper = 2
    scissors = 3

    playAgain = True

    while playAgain == True:
        if person == computer:
            print("Tie")
            tie += 1
            repeat = input("Play again? Y/N")
            if repeat != "y":
                print(f"Score = My score: {computerScore} / Your Score: {personScore} / Ties: {tie}")
                break 
        elif person == 1 and computer == 2:
            print("I win!")
            computerScore += 1
            repeat = input("Play again? Y/N")
            if repeat != "y":
                print(f"Score = My score: {computerScore} / Your Score: {personScore} / Ties: {tie}")
                break
        elif person == 2 and computer == 3:
            print("I win!")
            computerScore += 1
            repeat = input("Play again? Y/N")
            if repeat != "y":
                print(f"Score = My score: {computerScore} / Your Score: {personScore} / Ties: {tie}")
                break
        elif person == 3 and computer == 1:
            print("I win!")
            computerScore += 1
            repeat = input("Play again? Y/N")
            if repeat != "y":
                print(f"Score = My score: {computerScore} / Your Score: {personScore} / Ties: {tie}")
                break
        elif person == 1  and computer == 3:
            print("You win!")
            personScore += 1
            repeat = input("Play again? Y/N")
            if repeat != "y":
                print(f"Score = My score: {computerScore} / Your Score: {personScore} / Ties: {tie}")
                break
        elif person == 2 and computer == 1:
            print("You win!")
            personScore += 1
            repeat = input("Play again? Y/N")
            if repeat != "y":
                print(f"Score = My score: {computerScore} / Your Score: {personScore} / Ties: {tie}")
                break
        elif person == 3 and computer == 2:
            print("You win!")
            personScore += 1
            repeat = input("Play again? Y/N")
            if repeat != "y":
                print(f"Score = My score: {computerScore} / Your Score: {personScore} / Ties: {tie}")
                break

