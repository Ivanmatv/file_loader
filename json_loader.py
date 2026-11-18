from loader import Loader


class JsonLoader(Loader):
    def __init__(self):
        self.__file = ""

    def load(self) -> str:
        return f"файл - {self.__file} - загружен"

    def serialize(self, file: str) -> None:
        self.__file = file +".json"


