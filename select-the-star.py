import random
import sys
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def user_input(information):
    guess = input(information)

    if guess.lower() == "exit":
        sys.exit()
    elif guess.lower() == "y":
        pass
    else:
        try:
            return int(guess)
        except ValueError:
            print(f"{guess} is not an option.")

    return None

def random_location(row_column):
    star_row = random.randrange(1, row_column + 1)
    star_column = random.randrange(1, row_column + 1)

    row_column_index = 1

    print(f"There are {row_column} rows and columns.\n")
    
    print("*" + "--" * row_column + "-*")

    for val in range(1, row_column + 1):
        if star_row == val:
            print("| " + ("+ " * (star_column - 1)) + "* " + ("+ " * (row_column - star_column)) + "|")
        else:
            print("| " + "+ " * row_column + "|")

    print("*" + "--" * row_column + "-*\n")

    return star_row, star_column

def main():
    print("Welcome to Select_the_Star!\n")

    user_input("Start Game?\n'y' or 'exit': ")

    row_column = 10

    while True:
        clear_screen()

        row, column = random_location(row_column)

        chance = 3

        while chance > 0:
            guess_row = user_input("Guess the star row: ")
            if guess_row is None:
                continue

            if guess_row == row:
                print(f"Success! The row is {guess_row}.\n")

                guess_column = user_input("Guess the star column: ")

                if guess_column is None:
                    continue

                elif guess_column == column:
                    print(f"Success! The column is {guess_column}.\n")

                    break
                else:
                    chance -= 1

                    if chance > 0:
                        print(f"Try again. You have {chance} chances left.\n")
                    else:
                        print("You are out of attempts!")
            else:
                chance -= 1

                if chance > 0:
                    print(f"Try again. You have {chance} chances left.\n")
                else:
                    print("You are out of attempts!")

        if chance <= 0:
            break

        row_column += 5

if __name__ == "__main__":
    main()

    clear_screen()

    print("Thanks for playing!")
