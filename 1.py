import csv
import datetime

with open("scientist.txt", encoding="utf-8") as f:
    s = list(csv.DictReader(f, delimiter="#"))
    scientists = {}
    c = ""
    s = sorted(s, key=lambda x: datetime.date(list(map(int, x["date"].split("-")))[0],
                                              list(map(int, x["date"].split("-")))[1],
                                              list(map(int, x["date"].split("-")))[2]))
    # Отсортировать список лекарств по дате
    print("Разработчиками Аллопуринола были такие люди")
    for i in s:
        if i["preparation"] not in scientists.keys():  # Добавить неуспользуемый элемент в список
            scientists[i["preparation"]] = i
        if i["preparation"] == "Аллопуринол":          # Вывести создателей аллопуринола
            if c == "":
                c = i["ScientistName"]
            print(i["ScientistName"] + " - " + i["date"])
    print(f'Оригинальный рецепт принадлежит: {i["ScientistName"]}')
    scientists = list(scientists.values())

with open("scientist_origin.txt", "w", encoding="utf-8", newline="") as f:  # Файл с оригинальными авторами
    writer = csv.DictWriter(f, fieldnames=["ScientistName", "preparation", "date", "components"], delimiter="#")
    writer.writeheader()
    writer.writerows(scientists)
