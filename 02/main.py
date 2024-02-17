import random

print("---------------------------------")
print("\t Number Guessing")
print("---------------------------------")
print()

the_number = random.randint(0, 100)
name = input("Please Enter Your Name: ")
guess = -1
while guess != the_number:
    guess_text = input("{}, guess a number between 0 ,100: ".format(name))

    guess = int(guess_text)
    if guess < the_number:
        print("sorry {}, your guess of {} is too low".format(name, guess))
    elif guess > the_number:
        print("sorry {}, your guess of {} is too high".format(name, guess))
    else:
        print("you win")
