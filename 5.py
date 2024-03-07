import csv
import random


def hash(s):               # Хеширование
    a = list(range(1024))
    random.shuffle(a)
    s = s.split()
    s = [ord(x[0]) % 1024 for x in s]
    return (a[s[0]] + a[s[1]] + a[s[2]]) % 2048


with open("scientist.txt", encoding="utf-8") as f:
    s = list(csv.DictReader(f, delimiter="#"))
    for i in s:
        i["hash"] = hash(i["ScientistName"])

with open("cientist_with_hash.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ScientistName", "preparation", "date", "components", "hash"], delimiter="#")
    writer.writeheader()
    writer.writerows(s)
