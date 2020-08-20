a,b = map(int,input().split())
set1 = set()
result = []

for i in range(a) :
    name = input()
    set1.add(name)

for i in range(b) :
    name = input()
    if name in set1 :
        result.append(name)

result.sort()
print(len(result))
for i in range(len(result)) :
    print(result[i])


    