
import json

with open("teste.json",encoding="utf-8") as b:
    arquivo=json.load(b)


print(arquivo["Idade"])



