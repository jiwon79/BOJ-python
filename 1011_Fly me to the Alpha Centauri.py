n = int(input())
for i in range(n):
  start, end = map(int, input().split(' '))
  length = end - start
  m = int(length**0.5)
  
  if (length == m**2):
    print(2*m-1)
  elif (length <= m*m+m):
    print(2*m)
  else:
    print(2*m+1)
  
  