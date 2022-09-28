import random

top_range = input("Enter a number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Enter a number greater than 0 next time")
        quit()
else:
    print("Enter a number next time !")
    quit()
random_number = random.randint(0, top_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it !")
        break
    elif user_guess > random_number :
        print("Too high !")
    else:
        print("Too low !")

print("You got" , guess , "correctly")

