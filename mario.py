def main():
    print_column(3)
    print_row(3)
    print_square(5)

def print_column(height):
    for i in range(height):
        print("#")

def print_row(width):
    print("#" * width)
    
def print_square(size):

    # for each row in square
    for i in range(size):

        # for each brick in row
        for j in range(size):

            # print brick
            print("#", end="")
        print()

    print_square_second_way(3)

def print_square_second_way(size):
    for i in range(size):
        print_row_second_way(size)

def print_row_second_way(width):
    print("#" * width)

main()