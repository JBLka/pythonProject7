import csv
import random
from string import ascii_letters, digits

def hash(s):
    a = list(range(1024))
    random.shuffle(a)
    s = s.split()
    s = [ord(x[0]) % 1024 for x in s]
    return a[s[0]] + a[s[1]] + a[s[2]]

with open("scientist.txt", encoding="utf-8") as f:
    s = list(csv.DictReader(f, delimiter="#"))
    for i in s:
        name = i["ScientistName"]
        i["hash"] = hash(name)


with open("cientist_with_hash.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ScientistName","preparation", "date", "components", "hash"], delimiter = "#")
    writer.writeheader()
    writer.writerows(s)