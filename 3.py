import csv
import datetime

with open("scientist.txt", encoding="utf-8") as f:
    s = list(csv.DictReader(f, delimiter="#"))
    date = input()
    while date != "эксперимент":
        date = date.split('.')
        date = date[::-1]
        date = str(datetime.date(int(date[0]), int(date[1]), int(date[2])))  # Получаем введеную дату
        le = 0
        ri = len(s) - 1
        while le <= ri:
            center = (le + ri) // 2
            if date == s[center]['date']:
                scientist = s[center]
                scientist_name = scientist['ScientistName'].split()
                print(f'Ученый {scientist_name[0]} {scientist_name[1][0]}.{scientist_name[2][0]}.'
                      f' создал препарат: {scientist["preparation"]} - {scientist["date"]}')
                break
            if date > s[center]['date']:
                le = center + 1
            else:
                ri = center - 1
        date = input()
