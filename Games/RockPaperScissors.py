import random

while True:
    def play():
        win = 0
        loss = 0
        tie = 0

        user = input(" Choose ,r for rock ,p for paper ,s for scissors")
        computer = random.choice(["r", "p", "s"])
        # ground rules
        # r>s , s>p, p>r
        if user == computer:

            return "It\'s a tie"

        if is_win(user, computer):
            return "You win"

        return "You Lost!"


    def is_win(player, opponent):
        # return true id player wins
        if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
                or (play == "p" and opponent == "r"):
            return True


    print(play())

    playagain = input("Do want to play again(y/n):")
    if playagain != "y":
        print("bye!!")
        break
