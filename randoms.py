import random
import json

mylist = []

for i in range (0,10000):
    a = random.uniform(1000, 9999)
    mylist.append(float(f"{a:.2f}"))

#print(mylist)

try:
    with open("file.txt", "x", encoding="utf-8") as f:
        f.write(str(mylist))

except FileExistsError:
    print("file.txt already exists, exclusive creation aborted.")

with open("file.txt", "r") as f:
    content = f.read()
    mylist = eval(content)
    print(type(mylist), mylist)