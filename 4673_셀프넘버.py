self_number = [[i+1,0] for i in range(10000)]
self = []

def make_number(n) :
    sum = n
    while n>= 1 :
        sum += n%10
        n = n//10
    return sum

for i in range(1,10001) :
    m = make_number(i)
    if m <= 10000 :
        self_number[m-1][1] = 1
    if self_number[i-1][1] == 0 :
        self += [i]

for i in range(len(self)) :
    print(self[i])