from random import randint
from piece import DoubleLetterPiece, DoubleWordPiece, TripleLetterPiece, TripleWordPiece, NormalPiece

class PieceDecoratorFactory(object):
    # Props is a mapping constructor -> count to create
    def __init__(self, props):
        self.props = props

    def decorate_one(board, constructor):
        x = randint(0, len(board.tiles[0])-1)
        y = randint(0, len(board.tiles)-1)
        while type(board.tiles[y][x]) != NormalPiece:
            x = randint(0, len(board.tiles[0])-1)
            y = randint(0, len(board.tiles)-1)
        board.tiles[y][x].decorate(constructor)

    # Mutates the board as desired
    def decorate(board):
        for key in self.props:
            for i in range(self.props[key]):
                self.decorate_one(board, key)

class RoundOnePieceDecoratorFactory(PieceDecoratorFactory):
    def __init__(self):
        super().__init__({
            DoubleLetterPiece: 2,
            DoubleWordPiece: 1
        })
