from collections import defaultdict
from colorama import Style, Fore

class Piece(object):
    def __init__(self, letter, point_value, multiplier, color):
        if type(letter) != str or len(letter) != 1:
            raise Exception("A piece's value must be a single character")
        
        self.letter = letter.upper()
        self.neighbours = defaultdict(list)
        self.point_value = point_value
        self.multiplier = multiplier
        self.color = color

    def __str__(self):
        return self.color + self.letter + Style.RESET_ALL

    def connect(self, other):
        self.neighbours[other.letter].append(other)
        other.neighbours[self.letter].append(self)
    
    def clear_connections(self):
        self.neighbours = defaultdict(list)

    def generate_score(self, word):
        best = (0, [])
        possible = self.generate_score_helper(word)
        for possibility in possible:
            score = Piece.compute_point_value(possibility)
            if score > best[0]:
                best = (score, possibility)
        return best

    def generate_score_helper(self, word, visited=set()):
        if self in visited:
            return []

        if len(word) == 1:
            return [[self]] if word == self.letter else []
        
        if word[0] != self.letter:
            return []
        
        visited.add(self)
        possibilities_per_tile = [x for x in [neighbour.generate_score_helper(word[1:], visited) for neighbour in self.neighbours[word[1]]] if len(x) > 0]
        visited.remove(self)

        found = []
        for possibilities in possibilities_per_tile:
            for possibility in possibilities:
                found.append([self, *possibility])
        return found

    @property
    def value(self):
        return (lambda x: x*self.multiplier, lambda x: x+self.point_value, self)

    @staticmethod
    def compute_point_value(pieces):
        val = 0
        operation_pairs = [piece.value for piece in pieces]

        for operation_pair in operation_pairs:
            val = operation_pair[1](val)

        for operation_pair in operation_pairs:
            val = operation_pair[0](val)

        return val + max((len(pieces) - 4) * 5, 0)

    @staticmethod
    def from_string(s):
        const = None
        if len(s) == 1:
            const = NormalPiece
        else:
            if s[1:].lower() == '2l':
                const = DoubleLetterPiece
            if s[1:].lower() == '2w':
                const = DoubleWordPiece
            if s[1:].lower() == '3l':
                const = TripleLetterPiece
            if s[1:].lower() == '3w':
                const = TripleWordPiece
            s = s[0]
        return lambda x: const(s, x)
    
# A regular piece
class NormalPiece(Piece):
    def __init__(self, letter, point_value):
        super().__init__(letter, point_value, 1, Fore.WHITE)

    def decorate(self, constructor):
        return constructor(self.letter, self.point_value)

# The point value for this piece is twice what it would normally be
class DoubleLetterPiece(Piece):
    def __init__(self, letter, point_value):
        super().__init__(letter, 2*point_value, 1, Fore.GREEN)

# The point value for this piece is thrice what it would normally be
class TripleLetterPiece(Piece):
    def __init__(self, letter, point_value):
        super().__init__(letter, 3*point_value, 1, Fore.BLUE)

# Words including this letter are worth double
class DoubleWordPiece(Piece):
    def __init__(self, letter, point_value):
        super().__init__(letter, point_value, 2, Fore.YELLOW)

# Words including this letter are worth triple
class TripleWordPiece(Piece):
    def __init__(self, letter, point_value):
        super().__init__(letter, point_value, 3, Fore.RED)