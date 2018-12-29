from weighted_random_generator import WeightedRandomGenerator

# abstract class for the languages that you could play in...
# english will be the only language for now but this will make things extensible at least

class Language(object):
    def __init__(self, weight_map):
        m = max(weight_map.values())
        self.weighted_random_generator = WeightedRandomGenerator([(m - weight_map[key] + 1, key) for key in weight_map])

    @property
    def point_values(self):
        raise NotImplemented("Error! Point_values mapping must be implemented by the subclass")

    # returns a list of the valid letters that can be on tiles... useful for excluding letters that are not common in a certain language (e.g. Q in english)
    @property
    def letters(self):
        raise NotImplemented("Error! letters must be implemented by the subclass")

    def generate_letter(self):
        return self.weighted_random_generator.get_element()

class EnglishLanguage(Language):
    def __init__(self):
        super().__init__(self.point_values)

    @property
    def point_values(self):
        return {
            "A": 1,
            "B": 3,
            "C": 3,
            "D": 2,
            "E": 1,
            "F": 4,
            "G": 2,
            "H": 4,
            "I": 1,
            "J": 8,
            "K": 5,
            "L": 1,
            "M": 3,
            "N": 1,
            "O": 1,
            "P": 3,
            "R": 1,
            "S": 1,
            "T": 1,
            "U": 1,
            "V": 4,
            "W": 4,
            "X": 8,
            "Y": 4,
            "Z": 10
        }

    @property
    def letters(self):
        # all letters are valid in english but q
        return list(self.point_values.keys())