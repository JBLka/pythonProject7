import csv
import random
from string import ascii_letters, digits

with open("scientist.txt", encoding="utf-8") as f:
    s = list(csv.DictReader(f, delimiter="#"))
    for i in s:
        name = i["ScientistName"].split()
        i["login"] = name[0] + "_" + "" + name[1][0] + name[2][0]
        i["password"] = random.choices(ascii_letters + digits, k=10)
        random.shuffle(i["password"])
        i["password"] = "".join(i["password"])

with open("scientist_password.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ScientistName", "preparation", "date", "components", "login", "password"],
                            delimiter="#")
    writer.writeheader()
    writer.writerows(s)
