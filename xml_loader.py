from loader import Loader


class XmlLoader(Loader):
    def __init__(self):
        self.__file = ""

    def load(self) -> str:
        return f"файл - {self.__file} загружен"

    def serialize(self) -> None:
        self.__file = self.__file +".xml"
