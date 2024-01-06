from collections import deque
n, m = map(int,input().split())
arr = [list(map(int,input().strip())) for _ in range(n)] #.strip() : 한글자씩
visit = [[0 for _ in range(m)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(n, m):
    que = deque()
    que.append((0,0))
    visit[0][0] = 1

    while que:
        x, y = que.popleft()
        if (x == n-1 and y == m-1):
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<=nx<n and 0<=ny<m and visit[nx][ny] == 0 and arr[nx][ny]==1):
                que.append((nx,ny))
                visit[nx][ny] = visit[x][y] + 1

bfs(n,m)

print(visit[n-1][m-1])