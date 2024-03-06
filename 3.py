import csv
import datetime


with open("scientist.txt", encoding="utf-8") as f:
    s = list(csv.DictReader(f, delimiter="#"))
    t = input()
    while t != "эксперимент":
        dd, mm, yyyy = map(int, t.split("."))
        date = str(datetime.date(yyyy, mm, dd))
        for i in s:
            if i["date"] == date:
                name = i["ScientistName"].split()
                print(f'Ученый {name[0]} {name[1][0]}. {name[2][0]}. создал препарат: {i["preparation"]} - {date}')
        t = input()