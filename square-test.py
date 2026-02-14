import random

# Represent square on a board
class Square:
    def __init__(self, row, column):
        self.row = row
        self.column = column

# Map columns to numbers
columns = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8
}

# Reverse mapping for columns
columns_rev = {v: k for k, v in columns.items()}

# Determine the color of the square
def check_color(square):
    if (square.row + square.column) % 2 == 0:
        return "black"
    else:
        return "white"

# Quiz logic
def quiz():
    fails = 0
    print("type 'w' for white and 'b' for black.")
    while fails < 3:
        row = random.randint(1, 8)
        column = random.randint(1, 8)
        square = Square(row, column)
        color = check_color(square)

        answer = input(f"{columns_rev[column]}{row}: ")
        if answer.lower() == "w" and color == "white":
            print("Correct!")
        elif answer.lower() == "b" and color == "black":
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {color}.")
            fails += 1

    print("Game over! You have failed 3 times.")

if __name__ == "__main__":
    quiz()
