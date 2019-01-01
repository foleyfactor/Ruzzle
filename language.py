from weighted_random_generator import WeightedRandomGenerator

# abstract class for the languages that you could play in...
# english will be the only language for now but this will make things extensible at least

class Language(object):
    valid_word_path = "./valid_words/{0}.txt"

    def __init__(self):
        self.weighted_random_generator = WeightedRandomGenerator([(self.letter_distribution[key], key) for key in self.letter_distribution])
        self._valid_words = None

    @property
    def point_values(self):
        raise NotImplemented("Error! Point_values mapping must be implemented by the subclass")

    # returns a list of the valid letters that can be on tiles... useful for excluding letters that are not common in a certain language (e.g. Q in english)
    @property
    def letters(self):
        raise NotImplemented("Error! letters must be implemented by the subclass")

    @property
    def language_string(self):
        raise NotImplemented("Error! language_string must be implemented by the subclass")

    @property
    def letter_distribution(self):
        raise NotImplemented("Error! letter_distribution must be implemented by the subclass")

    @property
    def valid_words(self):
        if self._valid_words is None:
            with open(self.valid_word_path.format(self.language_string)) as f:
                self._valid_words = [x.strip() for x in f.readlines()]
        return self._valid_words

    def generate_letter(self):
        return self.weighted_random_generator.get_element()

class EnglishLanguage(Language):
    def __init__(self):
        super().__init__()

    @property
    def letter_distribution(self):
        return {
            "A": 14810,
            "B": 2715,
            "C": 4943,
            "D": 7874,
            "E": 21912,
            "F": 4200,
            "G": 3693,
            "H": 10795,
            "I": 13318,
            "J": 188,
            "K": 1257,
            "L": 7253,
            "M": 4761,
            "N": 12666,
            "O": 14003,
            "P": 3316,
            "Q": 205,
            "R": 10977,
            "S": 11450,
            "T": 16587,
            "U": 5246,
            "V": 2019,
            "W": 3819,
            "X": 315,
            "Y": 3853,
            "Z": 128
        }

    @property
    def point_values(self):
        return {
            "A": 1,
            "B": 4,
            "C": 4,
            "D": 2,
            "E": 1,
            "F": 4,
            "G": 3,
            "H": 4,
            "I": 1,
            "J": 10,
            "K": 5,
            "L": 1,
            "M": 3,
            "N": 1,
            "O": 1,
            "P": 4,
            "Q": 10,
            "R": 1,
            "S": 1,
            "T": 1,
            "U": 2,
            "V": 4,
            "W": 4,
            "X": 8,
            "Y": 4,
            "Z": 8
        }

    @property
    def letters(self):
        # all letters are valid in english but q
        return list(self.point_values.keys())

    @property
    def language_string(self):
        return "english"