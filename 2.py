import csv
import datetime
import random


def quicksort(n):                                     # Сортировка
    if len(n) <= 1:
        return n
    else:
        l_list = []
        m_list = []
        r_list = []
        x = random.choice([j for j in n])
        date = list(map(int, x["date"].split("-")))
        q = datetime.date(date[0], date[1], date[2])  # Случайная дата из списка
        for z in n:
            date = list(map(int, z["date"].split("-")))
            b = datetime.date(date[0], date[1], date[2])
            if b < q:
                l_list.append(z)                      # Открытия в этот день
            elif b > q:
                r_list.append(z)                      # Открытия в последующие дни
            else:
                m_list.append(z)                      # Открытия в предыдущие дни
        return quicksort(l_list) + m_list + quicksort(r_list)


with open("scientist.txt", encoding="utf-8") as f:
    s = list(csv.DictReader(f, delimiter="#"))
    s = quicksort(s)

with open("scientist.txt", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ScientistName", "preparation", "date", "components"], delimiter="#")
    writer.writeheader()
    writer.writerows(s)
