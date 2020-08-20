# print list function
def printList(list) :
    for i in range(len(list)) :
        print(list[i], end=" ")

n, m, start = map(int, input().split())

edge = [[] for i in range(n+1)]

for i in range(m) :
    v1, v2 = map(int, input().split())
    edge[v1].append(v2)
    edge[v2].append(v1)

# 여러 node에 연결되어 있을 경우 작은 node 부터 가기 위해서 정렬해둠
for i in range(1, n+1) :
    edge[i].sort()

# print DFS
visited = []
stack = [start]

while(len(stack) != 0) :
    node = stack[-1]
    del stack[-1]
    # 방문하지 않았을 경우에만 실행
    if not node in visited :
        # 작은 노드부터 가도록 stack에 거꾸로 넣음
        for i in range(len(edge[node])-1,-1,-1) :
            # 방문하지 않은 node만 stack에 넣음
            if not edge[node][i] in visited :
                stack.append(edge[node][i])
        visited.append(node)  
printList(visited)
print()

# print BFS
visited = []
queue = [start]

while(len(queue) != 0) :
    node = queue[0]
    del queue[0]
    # 방문하지 않았을 경우에만 실행
    if not node in visited :
        # 작은 노드부터 가도록 queue에 넣음
        for i in range(len(edge[node])) :
            # 방문하지 않은 node만 queue에 넣음
            if not edge[node][i] in visited:
                queue.append(edge[node][i])
        visited.append(node)
printList(visited)

