import heapq
m, n = map(int, input().split())
arr = [list(map(int,input())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
li = []

heapq.heappush(li,(0,0,0))
visit[0][0] = 1
res = 0

while li:
    cnt,x,y = heapq.heappop(li)

    if x ==n-1 and y==m-1:
        res = cnt
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if 0<=nx<n and 0<=ny<m and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            if arr[nx][ny] == 0:
                heapq.heappush(li, (cnt, nx, ny))
            else:
                heapq.heappush(li, (cnt+1, nx, ny))

print(res)