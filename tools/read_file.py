import json


class ReadFile:

    @staticmethod
    def read_file(way):
        with open(way) as text:
            data = json.load(text)
        return data
