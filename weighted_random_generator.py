from bisect import bisect_left
from random import randint

# takes a list of the form (weight, value) and provides the ability to choose a random
# object based on its weight
class WeightedRandomGenerator(object):
    def __init__(self, arr):
        total = 0
        self.prefix_array = []
        self.items = []
        for pair in arr:
            total += pair[0]
            self.prefix_array.append(total)
            self.items.append(pair[1])
        self.total = total

    def get_element(self):
        val = randint(1, self.total)
        ind = bisect_left(self.prefix_array, val)
        return self.items[ind]