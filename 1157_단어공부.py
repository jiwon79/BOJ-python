s = input().upper()
alphabetList = [0]*26

for i in range(len(s)) :
    alphabetList[ord(s[i]) - ord('A')] += 1

max = 0
count = 0
for i in range(26) :
    if alphabetList[i] > max :
        max = alphabetList[i]
        count = 1
        index = i
    if alphabetList[i] == max :
        count += 1

if count>2 : 
    print('?')
else :
    print(chr(index+ord('A')))
