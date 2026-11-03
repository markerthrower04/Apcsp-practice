import random

rock = 0
paper = 1
scissors = 2

options = [rock, paper, scissors]
options_str = ["rock", "paper", "scissors"]

def option_picker(choices):
    return random.choice(choices)


def get_player_input():
    player = -1
    while player == -1:
        user_input = int(input("Enter 0 for rock, 1 for paper, and 2 for scissors: "))
        if 0 <= user_input <= 2:
            player = user_input
    return player


def winner(p1,p2):
    if p1 == p2:
        winner = 0
    elif (p1 == 0 and p2 == 2) or ( p1 == 1 and p2 == 0) or (p1 == 2 and p2 == 1):
        winner = 1
    else:
        winner = 2
    return winner

def strat(num_rounds, bots_move):
    return (num_rounds + bots_move)  % 3

def human_strat():
    user_choice = ""
    while user_choice != "H" and user_choice != "S" :
        user_choice = input("Human strategy or computer strategy? H for human - S for  strategy: ").upper()
    return user_choice

def main():

    player_score = 0
    bot_score = 0
    rounds = 5

    user_choice = human_strat()

    while rounds != 0:
        
        bot = option_picker(options)
        
        if user_choice == "H":
            player = get_player_input()
        else:
            player = strat(rounds, bot)

        who_won = winner(player,bot)
        print(f"You chose: **{options_str[player]}** and the bot chose: **{options_str[bot]}**." )
        if who_won == 1:
            player_score += 1
            print("You won this round!")
        elif who_won == 2:
            bot_score += 1
            print("The bot won this round!")
        else:
            print("This round was a tie!")
        
        rounds -= 1
    print("player score: " + str(player_score))
    print("bot score: "+ str(bot_score ))
pass



if __name__ == "__main__":
    main()