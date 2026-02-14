import random

# Represent square on a board
class Square:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.color = check_color(self)

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

def generate_square():
    row = random.randint(1, 8)
    column = random.randint(1, 8)
    square = Square(row, column)
    color = check_color(square)
    return square