name = input("What's your name? ")

match name:
    case "Adi" | "Budi" | "Cici":
        print("Jakarta")
    case "Edi":
        print("Bandung")
    case _:
        print("Siapa?")