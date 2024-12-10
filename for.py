for i in [0, 1, 2]:
    print(i)

for i in range(3):
    print(i)

for _ in range(3):
    print("meow")

print("meow" * 3)

while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break

    return n

def meow(n):
    for i in range(n):
        print("miaow")

main()