
def collatz(number):
    repeat = 0 
    counter = 1
    while repeat != 1:
        if (number % 2 == 0):
            number = (number // 2)
            print(number)
            counter += 1
            if number == 1:
                repeat += 1
                print(f"It took {counter} steps to reach 1.")

        else:
            number = ((number * 3) + 1)
            print(number)
            if number == 1:
                repeat += 1
            
number = int(input("Please choose a number: "))
collatz(number)