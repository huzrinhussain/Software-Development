
user = None
i = None
total = 0

for i in range(5):
    user = int(input("Enter Number"))
    total += user
    i += 1
print("Total", total)
print("Count", i)