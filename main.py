from file_loader.json_loader import JsonLoader
from file_loader.xml_loader import XmlLoader


def load_file(loader, file):
    return loader.load(file)

json_loader = JsonLoader()
xml_loader = XmlLoader()

home_work = "домашняя_работа"

print(load_file(loader=json_loader, file=home_work))
print(load_file(loader=xml_loader, file=home_work))
