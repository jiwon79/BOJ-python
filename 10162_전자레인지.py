time = int(input())

# print list index
def printList(list) :
    for i in range(len(list)) :
        print(list[i], end=" ")

# A,B,C button의 time
buttonList = [300, 60, 10]
buttonNum = [0,0,0]

while (time >= 300) :
    buttonNum[0] += 1
    time -= 300

while (time >= 60) :
    buttonNum[1] += 1
    time -= 60

while (time >= 10) :
    buttonNum[2] += 1
    time -= 10

# A,B,C로 표현되지 않는경우
if (time % 10 != 0) :
    print(-1)
else :
    printList(buttonNum)
