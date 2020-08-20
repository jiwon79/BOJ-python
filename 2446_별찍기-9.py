n = int(input())

for i in range(n) :
    for j1 in range(i) :
        print(' ',end='')
    for j2 in range(2*(n-i)-1) :
        print('*',end='')
    print()
for i in range(n-1) :
    for j1 in range(n-i-2) :
        print(' ', end='')
    for j2 in range(2*i+3) :
        print('*',end='')
    print()