import random

number = random.randint(1,10)
print("Welcome to guess the number game! You have 3 tries to guess. Good luck:)")

for i in range(0,3):
    user = int(input("Guess the number: "))
    if user==number:
        print("Hurray!")
        print("You guessed right, the number was " + str(number) + ".")
        break
    elif user>number:
         print("You guessed too high..")
         print('You have ' + str(3-(i+1)) + ' tries left.')
    elif user<number:
         print("You guessed too low..")
         print('You have ' + str(3-(i+1)) + ' tries left.')
else:
    print("You lost! The number was " + str(number) + ".")