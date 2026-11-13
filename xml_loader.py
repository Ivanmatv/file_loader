class XmlLoader:
    def __init__(self, file):
        self.file = file

    def load(self) -> str:
        return f"файл - {self.file}.xml загружен"