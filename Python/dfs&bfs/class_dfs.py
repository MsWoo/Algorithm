n, m = map(int, input().split())

graph = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]
visited = [False for _ in range(n+1)]
cnt = 0

def dfs(vertex):
    global cnt
    global visited

    for cur_v in range(1, n+1):
        if graph[vertex][cur_v] == 1 and visited[cur_v] == False:
            visited[cur_v] = True
            cnt += 1
            dfs(cur_v)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

visited[1] = True
dfs(1)

print(cnt)