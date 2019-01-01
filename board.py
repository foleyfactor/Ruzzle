from piece import NormalPiece, Piece
from collections import defaultdict
from random import choice

class Board(object):
    def __init__(self, tiles, language):
        self.language = language
        self.tiles = [[NormalPiece(letter, language.point_values[letter]) for letter in row] for row in tiles]
        self.connect_tiles()

    def clear_connections(self):
        for row in self.tiles:
            for tile in row:
                tile.clear_connections()

    def connect_tiles(self):
        self.map = defaultdict(list)
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                p = self.tiles[i][j]
                self.map[p.letter].append(p)
                if i > 0:
                    if j > 0:
                        self.tiles[i][j].connect(self.tiles[i-1][j-1])
                    if j < len(self.tiles[0])-1:
                        self.tiles[i][j].connect(self.tiles[i-1][j+1])
                    self.tiles[i][j].connect(self.tiles[i-1][j])
                if j > 0:
                    self.tiles[i][j].connect(self.tiles[i][j-1])

    def is_valid_word(self, word):
        return self.score_word(word) > 0
    
    def score_word(self, word):
        best_score = (0, [])
        for row in self.tiles:
            for tile in row:
                score = tile.generate_score(word)
                if score[0] > best_score[0]:
                    best_score = score
        return best_score

    def __str__(self):
        return "\n".join([" ".join([str(x) for x in row]) for row in self.tiles])

    @staticmethod
    def generate_board(language, size=4):
        board = [[language.generate_letter() for j in range(size)] for i in range(size)]
        return Board(board, language)

    @staticmethod
    def from_pieces(tiles, language):
        b = Board([[]], language)
        b.tiles = [[Piece.from_string(letter)(language.point_values[letter[0]]) for letter in row] for row in tiles]
        b.clear_connections()
        b.connect_tiles()
        return b
