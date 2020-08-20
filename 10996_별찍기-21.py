n = int(input())

for i in range(n) :
    for j1 in range(n) :
        if j1%2 == 1 :
            print(' ',end='')
        else :
            print('*',end='')
    print()
    for j1 in range(n) :
        if j1%2 == 1 :
            print('*',end='')
        else :
            print(' ',end='')
    print()
    