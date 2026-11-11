from json_loader import JsonLoader
from xml_loader import XmlLoader


home_work = "домашняя_работа"
json_loader = JsonLoader(home_work)
xml_loader = XmlLoader(home_work)

print(json_loader.load())
print(xml_loader.load())