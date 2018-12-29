from piece import NormalPiece
from point_retriever import PointRetriever
from collections import defaultdict

class Board(object):
    def __init__(self, tiles):
        self.point_retriever = PointRetriever("english")
        self.tiles = [[NormalPiece(letter, self.point_retriever.get(letter)) for letter in row] for row in tiles]
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
