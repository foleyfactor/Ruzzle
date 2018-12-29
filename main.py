from colorama import init
from board import Board

if __name__ == "__main__":
    init()

    b = Board([
        ["C", "a", "t"],
        ["d", "a", "d"],
        ["c", "a", "n"]
    ])

    print(str(b))