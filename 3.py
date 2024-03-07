import csv
import datetime

with open("scientist.txt", encoding="utf-8") as f:
    reader = list(csv.DictReader(f, delimiter="#"))
    request = input()
    while request != "эксперимент":
        request = request.split('.')
        request = request[::-1]
        request = str(datetime.date(int(request[0]), int(request[1]), int(request[2])))

        left = 0
        right = len(reader) - 1
        while left <= right:
            center = (left + right) // 2
            if request == reader[center]['date']:
                scientist = reader[center]
                scientist_name = scientist['ScientistName'].split()
                print(f'Ученый {scientist_name[0]} {scientist_name[1][0]}.{scientist_name[2][0]}.'
                      f' создал препарат: {scientist["preparation"]} - {scientist["date"]}')
                break
            if request > reader[center]['date']:
                left = center + 1
            else:
                right = center - 1
        request = input()
