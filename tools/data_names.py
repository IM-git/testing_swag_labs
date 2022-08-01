from patterns.singleton import Singleton
from tools.read_file import ReadFile

PATH = 'tools/data_names.json'


class DataNames(metaclass=Singleton):

    @staticmethod
    def get_list_names():
        return ReadFile.read_file(PATH)


if __name__ == '__main__':
    print(DataNames.get_list_names())
