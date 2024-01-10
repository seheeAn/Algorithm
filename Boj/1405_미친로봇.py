tmp = list(map(int,input().split()))
n, way = tmp[0], tmp[1:] 

visit = [[0 for _ in range(29)] for _ in range(29)]
dx = [1,-1,0,0] #동서남북
dy = [0,0,1,-1]

res = 0

def dfs(x,y,p,cnt):
    global res

    if cnt == n:
        res += p
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if visit[nx][ny] == 0:
            #backtracking
            visit[nx][ny] = 1
            dfs(nx,ny,p*(way[i]/100),cnt+1)
            visit[nx][ny] = 0

visit[14][14] = 1 #시작 위치 방문!
dfs(14,14,1,0)

print(res)