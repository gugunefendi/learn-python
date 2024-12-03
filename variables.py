def get_guess():
    guess = input("Enter a guess: ")
    return guess

# print(get_guess())

def main():
    guess = get_guess()
    if guess == "fifty":
        print("Correct!")
    else:
        print("Incorrect")

main()