import csv
import datetime


with open("scientist.txt", encoding="utf-8") as f:
    s = list(csv.DictReader(f, delimiter="#"))
    scientists = {}
    s = sorted(s, key=lambda x: datetime.date(list(map(int, x["date"].split("-")))[0], list(map(int, x["date"].split("-")))[1], list(map(int, x["date"].split("-")))[2]))

with open("scientist.txt", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ScientistName","preparation", "date", "components"], delimiter = "#")
    writer.writeheader()
    writer.writerows(s)