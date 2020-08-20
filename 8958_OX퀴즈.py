n = int(input())
list = []

for i in range(n) :
    s = input()
    list.append(s)

for i in range(n) :
    o = True
    conti = 1
    sum = 0
    
    for j in range(len(list[i])) :
        if list[i][j] == 'O' :
            sum += conti
            conti += 1
        else :
            conti = 1
    print(sum)