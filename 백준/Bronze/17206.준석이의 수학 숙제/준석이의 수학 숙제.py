n = int(input())
list = input().split()

for i in range(n) :
    thr = int(list[i])//3
    sev = int(list[i])//7
    two = int(list[i])//21
    
    print(thr*(thr+1)*3//2 + sev*(sev+1)*7//2 - two*(two+1)*21//2)