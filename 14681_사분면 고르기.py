a = int(input())
b = int(input())

def quadrant(a,b) :
    if a>0 :
        if b>0 :
            return 1
        return 4
    if b>0 :
        return 2
    return 3

print(quadrant(a,b))