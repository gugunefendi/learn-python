def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid a difficulty")
        return

    players = input("Single-player or Multiplayer? ")
    if not (players == "Multiplayer" or players == "Single-player"):
        print("Enter a valid a number of players")
        return

    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayers":
        recommend("Hearts")
    else:
        recommend("Clock")

def recommend(game):
    print("You might like", game)

main()