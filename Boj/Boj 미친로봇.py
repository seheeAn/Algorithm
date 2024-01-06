n, ea, we, so, no = map(int,input().split())
visit = [[0 for _ in range(n)] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if visit[nx][ny] == 0:
            #backtracking
            visit[nx][ny] = 1
            bfs(nx,ny)
            visit[nx][ny] = 0
        
        else:
            