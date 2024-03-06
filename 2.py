import csv
import datetime
import random

def quicksort(n):
    if len(n) <= 1:
        return n
    else:
        l_list = []
        m_list = []
        r_list = []
        x = random.choice([j for j in n])
        q = datetime.date(list(map(int, x["date"].split("-")))[0], list(map(int, x["date"].split("-")))[1], list(map(int, x["date"].split("-")))[2])
        for z in n:
            b = datetime.date(list(map(int, z["date"].split("-")))[0], list(map(int, z["date"].split("-")))[1], list(map(int, z["date"].split("-")))[2])
            if b < q:
                l_list.append(z)
            elif b > q:
                r_list.append(z)
            else:
                m_list.append(z)
        return quicksort(l_list) + m_list + quicksort(r_list)

with open("scientist.txt", encoding="utf-8") as f:
    s = list(csv.DictReader(f, delimiter="#"))
    scientists = {}
    s = quicksort(s)

with open("scientist.txt", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ScientistName","preparation", "date", "components"], delimiter = "#")
    writer.writeheader()
    writer.writerows(s)