import random

print("This is a number gussing game. \nThe computer make a random number and you need to gess what the no is. \nThe no of time you gessed to make it right will be displayed on the screen. ")

#asking the user to type the number so that computer can generate random number
top_of_range = input("Type a number between(1-10): ")

#checking the user input whether it is a no and greater than 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please enter a no greater than 0")
        quit()

else:
    print("please type a next time")
    quit()

#generating random number and checking whether the user guess is above or below the random number
random_no = random.randint(1,top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if  0> user_guess >10 :
            print("please,Enter a no between(1-10)")
            continue
        


    if user_guess < random_no:
        print("you where below the number")
    elif user_guess > random_no:
        print("you were above the number")
    else:
        print("you got it")
        break

print("you got it in", guesses, "gusses")
    



