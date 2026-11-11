class JsonLoader:
    def __init__(self, file):
        self.file = file

    def load(self):
        return f"файл - {self.file}.json загружен"