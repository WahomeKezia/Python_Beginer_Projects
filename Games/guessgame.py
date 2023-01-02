import random

# start my function

def guess():
    #declare my valuebles
    guess=0
    random_number=random.randint(1,15)
    #global playagain="Y"
    while guess!=random_number:
        guess = int(input("Enter your Guess: "))
        if random_number < guess:
            print("Your guess Number is too high!")
        elif random_number > guess:
            print("Your guess Number is too low!")
# using and else would still work but since I used !=
# I should just using the indentation , Python perks
#   else:
    # print(f"correct number!The guess number is {random_number}")

    print(f"correct number!The guess number is {random_number}")

guess()
print("********************\n")
# Game two ,  Computer guessing game
print("Now it's computer's turn to guess a random correct number")
def comp_game(x):
    low=1
    high=x
    feedback=""
    while feedback !="c":
        guess= random.randint(low,high)
        feedback =input(f"Is {guess} too high (H) , too low(L) or correct")
        if feedback=="H":
            high=guess-1
        elif feedback=="L":
            low=guess+1
    print("The computer got it right!")

comp_game(10)











