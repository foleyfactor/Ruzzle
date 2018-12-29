from piece import NormalPiece
from collections import defaultdict
from random import choice

class Board(object):
    def __init__(self, tiles, language):
        self.tiles = [[NormalPiece(letter, language.point_values[letter]) for letter in row] for row in tiles]
        self.map = defaultdict(list)
        for i in range(len(tiles)):
            for j in range(len(tiles[0])):
                p = self.tiles[i][j]
                self.map[p.letter].append(p)
                if i > 0:
                    if j > 0:
                        self.tiles[i][j].connect(self.tiles[i-1][j-1])
                    if j < len(tiles[0])-1:
                        self.tiles[i][j].connect(self.tiles[i-1][j+1])
                    self.tiles[i][j].connect(self.tiles[i-1][j])
                if j > 0:
                    self.tiles[i][j].connect(self.tiles[i][j-1])

    def is_valid_word(self, word):
        return any([any([piece.can_spell(word) for piece in row]) for row in self.tiles])

    def __str__(self):
        return "\n".join([" ".join([str(x) for x in row]) for row in self.tiles])

    @staticmethod
    def generate_board(language, size=4):
        board = [[language.generate_letter() for j in range(size)] for i in range(size)]
        return Board(board, language)

