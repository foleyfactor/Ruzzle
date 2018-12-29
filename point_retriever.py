class PointRetriever(object):
    def __init__(self, language):
        self.file_name = "{0}_point_values.json".format(language)
        self._data = None

    def get(self, letter):
        letter = letter.upper()
        return self.data[letter]
    
    @property
    def data(self):
        if self._data is None:
            import json
            with open(self.file_name, 'r') as f:
                self._data = json.loads("".join(f.readlines()).strip())
        return self._data