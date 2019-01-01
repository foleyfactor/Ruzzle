class BoardSolver(object):
    def __init__(self, board):
        self.board = board
        self._available_words = None

    def solve(self):
        if self._available_words is None:
            valid_words = self.board.language.valid_words
            found_words = []
            for word in valid_words:
                score = self.board.score_word(word)
                if score[0] > 0:
                    found_words.append((score[0], word, score[1]))
            self._available_words = sorted(found_words, key=lambda x: -1*x[0])


        return self._available_words