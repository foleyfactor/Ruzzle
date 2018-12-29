from colorama import init
from board import Board
from piece_factory import RoundOnePieceDecoratorFactory, RoundTwoPieceDecoratorFactory, RoundThreePieceDecoratorFactory
from language import EnglishLanguage

if __name__ == "__main__":
    init()

    b = Board.generate_board(EnglishLanguage())

    df = RoundThreePieceDecoratorFactory()
    df.decorate(b)

    print(str(b))