import random

# function to simulate a roll of a die
def roll_dice():
    return random.randint(1, 6)

# function to simulate a game of "Roll Dice"
def play_game():
    # set initial score to 0
    score = 0
    # simulate rolling the die 5 times
    for i in range(5):
        # roll the die
        roll = roll_dice()
        # add the roll to the score
        score += roll
        # print the roll
        print("Roll {}: {}".format(i+1, roll))
    # print the final score
    print("Final Score: {}".format(score))
    # determine if the player wins or loses
    if score > 15:
        print("You Win!")
    else:
        print("You Lose!")
