def solution(maps):
    answer = 0
    que = []
    N = len(maps)
    M = len(maps[0])
    _maps = [["X" for _ in range(M+2)] for _ in range(N+2)]
    for i in range(N):
        for j in range(M):
            _maps[i+1][j+1] = maps[i][j]
            if _maps[i+1][j+1] == "S":
                que.append([i+1, j+1, 0, 0]) #row,col,isL,time
            
    visit = [] #list형태로 확인해보자...
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    
    def bfs(que, end):
        while que:
            r,c,l,t = que.pop(0)
            if _maps[r][c] == end:
                return [r,c,1,t]
            
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if _maps[nr][nc] != "X" and [nr,nc,l] not in visit:
                    visit.append([nr,nc,l])
                    que.append([nr,nc,l,t+1])
        
        return [-1,-1,-1,-1]
    
    next_que = []
    next_que.append(bfs(que,"L"))
    if next_que[0] == [-1,-1,-1,-1]:
        return -1
    
    res_li = bfs(next_que, "E")
    if res_li[0] == -1:
        return -1

    return res_li[3]