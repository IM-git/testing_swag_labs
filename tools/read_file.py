import json


class ReadFile:

    @staticmethod
    def read_file(way):
        with open(way) as text:
            data = json.load(text)
        return data


if __name__ == '__main__':
    PATH = 'data_names.json'
    print(ReadFile.read_file(PATH))
