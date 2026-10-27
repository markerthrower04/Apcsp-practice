from game_status import clamp, make_bar


maximum = 40
for shield in (0, 20, 40):
    shown_shield = clamp(shield, 0, maximum)
    bar = make_bar(shown_shield, maximum)
    print("Shield  " + bar + " " + str(shown_shield) + "/" + str(maximum))
