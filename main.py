from json_loader import JsonLoader
from xml_loader import XmlLoader


home_work = "домашняя_работа"
json_loader = JsonLoader()
xml_loader = XmlLoader()

def load_file(file_name: str, formatter):
    formatter.serialize(file_name)
    print(formatter.load())


load_file(file_name=home_work, formatter=json_loader)
load_file(file_name=home_work, formatter=xml_loader)
