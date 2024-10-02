#!/usr/bin/env python3
"""That was to be able to run the file as a python script azn : ./main.py"""
name = input("Hey type your name: ")
print(f"Hello {name}, welcome to the game")

should_we_play = input("Do you want to play? (yes/no) ").lower()
if should_we_play == 'y' or should_we_play == 'yes':
    print('We are gonna play!')

    direction = input("Do you want to go right or left? (left/right) ").lower()
    if direction == 'right':
        choice = input("Okay, now you see a bridge, do you want to swim under it or cross it? (swim/cross) ").lower()
        if choice == 'swim':
            print("You got bitten by an aligator, you die... game over")
        else:
            print("You reached the other side and found the gold... You win")
    elif direction == 'left':
        print("Okay we went left and fell of a cliff, game over, try again.")
    else:
        print("Sorry not a valid reply, you die!")
else:
    print("Sad to see you leave")
