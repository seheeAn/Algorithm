from collections import deque

n, m = map(int, input().split())
map_list = []
visit = [[0 for i in range(m)] for j in range(n)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    map_list.append(list(map(int, input().split())))

def bfs(x,y):
    cnt = 0
    que = deque()
    que.append((x,y))
    visit[x][y] = 1

    while que:
        x, y = que.popleft()
        cnt += 1

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m and map_list[nx][ny] == 1:
                if (visit[nx][ny] == 0):
                    que.append((nx,ny))
                    visit[nx][ny] = 1
    
    return cnt

result = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if map_list[i][j] == 1 and visit[i][j]==0:
            result = max(result,bfs(i,j))
            cnt += 1

print(cnt)
print(result)