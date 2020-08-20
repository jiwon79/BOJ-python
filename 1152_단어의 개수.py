s = input()
n = 0
count = 0

for i in range(len(s)) :
    if s[i] == ' ':
        n += 1
        
if s[0] == ' ' :
    count += 1
if s[-1] == ' ' :
    count += 1
    
print(n-count+1)