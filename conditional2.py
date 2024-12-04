def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Single-player or Multiplayer? ")

    if (difficulty == "Difficult"):
        if (players == "Multiplayer"):
            recommend("Poker")
        elif (players == "Single-player"):
            recommend("Klondike")
        else:
            print("Enter valid players")
    elif (difficulty == "Casual"):
        if (players == "Multiplayer"):
            recommend("Hearts")
        elif (players == "Single-player"):
            recommend("Clock")
        else:
            print("Enter valid player")
    else:
        print("Enter valid difficulty")

def recommend(game):
    print("You might like", game)

main()