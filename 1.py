import csv
import datetime


with open("scientist.txt", encoding="utf-8") as f:
    s = list(csv.DictReader(f, delimiter="#"))
    scientists = {}
    new_f = []
    c = ""
    s = sorted(s, key=lambda x: datetime.date(list(map(int, x["date"].split("-")))[0], list(map(int, x["date"].split("-")))[1], list(map(int, x["date"].split("-")))[2]))
    print("Разработчиками Аллопуринола были такие люди")
    for i in s:
        if i["preparation"] not in scientists.keys():
            scientists[i["preparation"]] = i
        if i["preparation"] == "Аллопуринол":
            if c == "":
                c = i["ScientistName"]
            print(i["ScientistName"]+" - "+i["date"])
    print(f'Оригинальный рецепт принадлежит: {i["ScientistName"]}')
    scientists = list(scientists.values())

with open("scientist_origin.txt", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ScientistName","preparation", "date", "components"], delimiter = "#")
    writer.writeheader()
    writer.writerows(scientists)



    # for i in s:
    #     data = datetime.date(map(int, i["date"].split("-")))
    #     if len(new_f) == 0:
    #         new_f.append(i)
    #     elif
        # if i["preparation"] == "Аллопуринол":
        #     print(i["ScientistName"])
        # elif i["preparation"] not in scientists.keys():
        #     scientists[i["preparation"]] = i
        # elif int(scientists[i["preparation"]]["date"][:4]) > int(i["date"][:4]):
        #     scientists[i["preparation"]] = i
    # print(scientists)