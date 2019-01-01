from colorama import init 
from board import Board
from piece_factory import RoundOnePieceDecoratorFactory, RoundTwoPieceDecoratorFactory, RoundThreePieceDecoratorFactory
from piece import TripleLetterPiece as Tl, DoubleLetterPiece as Dl, NormalPiece as Nl
from language import EnglishLanguage
from board_solver import BoardSolver

if __name__ == "__main__":
    init()

    # tiles = []
    # for i in range(4):
    #     tiles.append([])
    #     for j in range(4):
    #         tiles[i].append(input().strip().upper())

    # b = Board.from_pieces(tiles, EnglishLanguage())

    b = Board.generate_board(EnglishLanguage())

    # df = RoundThreePieceDecoratorFactory()
    # df.decorate(b)

    print(str(b))

    bs = BoardSolver(b)
    solved = bs.solve()
    print("found {0} words! best are:".format(len(solved)))
    for i in range(10):
        print(solved[i][0], solved[i][1])