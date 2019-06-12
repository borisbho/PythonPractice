import random

results = ""

for i in range(50):
    results += str(random.randint(0,9))+" "

print(results)