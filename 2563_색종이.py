n = int(input())
count = 0
grid = [[0]*100 for i in range(100)]

for i in range(n) :
    x,y = map(int, input().split())
    
    for i in range(10) :
        for j in range(10) :
            grid[x+i][y+j] = 1

for i in range(100) :
    for j in range(100) :
        if grid[i][j] == 1 :
            count += 1

print(count)


