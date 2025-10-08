# Чтение JSON файла
import json

with open("sample-data.json", "r") as f:
    data = json.load(f)

# Просто выводим нужные данные
for item in data["imdata"]:
    info = item["l1PhysIf"]["attributes"]
    print(info["dn"], info["speed"], info["mtu"])
