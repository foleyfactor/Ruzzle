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

    def can_spell(self, word, visited=set()):
        if self in visited:
            return False
        if len(word) == 1:
            return word == self.letter
        visited.add(self)
        ret_val = any([neighbour.can_spell(word[1:], visited) for neighbour in self.neighbours[word[1]]])
        visited.remove(self)
        return ret_val

    @property
    def value(self):
        return (lambda x: x*self.multiplier, lambda x: x+self.point_value)

    @staticmethod
    def compute_point_value(pieces):
        val = 0
        operation_pairs = [piece.value for piece in pieces]

        for operation_pair in operation_pairs:
            val = operation_pair[1](val)

        for operation_pair in operation_pairs:
            val = operation_pair[0](val)

        return val
    
# A regular piece
class NormalPiece(Piece):
    def __init__(self, letter, point_value):
        super().__init__(letter, point_value, 1, Fore.WHITE)

    def decorate(self, constructor):
        return constructor(self.letter, self.point_value)

# The point value for this piece is twice what it would normally be
class DoubleLetterPiece(Piece):
    def __init__(self, letter, point_value):
        super().__init__(letter, 2*point_value, 1, Fore.BLUE)

# The point value for this piece is thrice what it would normally be
class TripleLetterPiece(Piece):
    def __init__(self, letter, point_value):
        super().__init__(letter, 3*point_value, 1, Fore.GREEN)

# Words including this letter are worth double
class DoubleWordPiece(Piece):
    def __init__(self, letter, point_value):
        super().__init__(letter, point_value, 2, Fore.YELLOW)

# Words including this letter are worth triple
class TripleWordPiece(Piece):
    def __init__(self, letter, point_value):
        super().__init__(letter, point_value, 3, Fore.RED)