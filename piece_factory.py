from random import randint
from piece import DoubleLetterPiece, DoubleWordPiece, TripleLetterPiece, TripleWordPiece, NormalPiece

class PieceDecoratorFactory(object):
    # Props is a mapping constructor -> count to create
    def __init__(self, props):
        self.props = props

    def decorate_one(self, board, constructor):
        x = randint(0, len(board.tiles[0])-1)
        y = randint(0, len(board.tiles)-1)
        while type(board.tiles[y][x]) != NormalPiece:
            x = randint(0, len(board.tiles[0])-1)
            y = randint(0, len(board.tiles)-1)
        board.tiles[y][x] = board.tiles[y][x].decorate(constructor)

    # Mutates the board as desired
    def decorate(self, board):
        for key in self.props:
            for i in range(self.props[key]):
                self.decorate_one(board, key)
        board.clear_connections()
        board.connect_tiles()

class RoundOnePieceDecoratorFactory(PieceDecoratorFactory):
    def __init__(self):
        super().__init__({
            DoubleLetterPiece: 2,
            DoubleWordPiece: 1
        })

class RoundTwoPieceDecoratorFactory(PieceDecoratorFactory):
    def __init__(self):
        super().__init__({
            DoubleLetterPiece: 2,
            DoubleWordPiece: 2
        })

class RoundThreePieceDecoratorFactory(PieceDecoratorFactory):
    def __init__(self):
        super().__init__({
            DoubleLetterPiece: 1,
            TripleLetterPiece: 2,
            DoubleWordPiece: 2,
            TripleWordPiece: 1
        })