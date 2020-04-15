
import random
play_game = 'y'
while(play_game == 'y'):
    answer = random.randint(1,100)
    try_number = int(input("Please enter your number"))
    counter = 1
    while try_number != answer:
        if try_number < answer:
            print("Your number is too small")
        else :
            print("Your number is too big")
        try_number = int(input("Please enter your number"))
        counter += 1
    print("You got it!you have tried" + str(counter) + "times")
    play_game = input("Continue?  y/n")
