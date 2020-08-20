bugger = []
drinks = []

for i in range(3) :
    a = int(input())
    bugger.append(a)
for i in range(2) :
    a = int(input())
    drinks.append(a)

print(min(bugger)+min(drinks)-50)