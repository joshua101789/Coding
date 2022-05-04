import random

x = random.randint(1, 100)
guesses = 0

print("I'm thinking of a number between 1-100... Try to guess it!!")
while True:
    try:
        guess=int(input("Guess: "))
        if guess ==x  and guesses == 0:
            print("CHEATER!!!! YOU GOT IT RIGHT ON THE FIRST GUESS!!")
            break
        elif guess == x and guesses != 0:
            print(f"Congratualtions your got it!!!! It only took {guesses} attempts!!")
            break
        elif guess > x:
            print("Not quite the number is smaller.")
            guesses += 1
        elif guess < x:
            print("Not quite the number is larger.")
            guesses += 1
        else:
            print("Try a number.....")
            guesses += 1
    except ValueError:
        print("Try guessing a number....")
        guesses += 1

        