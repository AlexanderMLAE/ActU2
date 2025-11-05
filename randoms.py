import random

mylist = []

for i in range (0,10000):
    a = random.uniform(1000, 9999)
    mylist.append(float(f"{a:.2f}"))

print(mylist)



 