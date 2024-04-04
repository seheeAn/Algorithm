def solution(maps):
    answer = []
    MAXr = len(maps)
    MAXc = len(maps[0])
    visit = [[0 for _ in range(MAXc)] for _ in range(MAXr)]
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    
    def bfs(row,col,cnt):
        que = [[row,col]]
        visit[row][col] = 1 
        while que:
            cr, cc = que.pop(0)
            for i in range(4):
                nr = dr[i] + cr
                nc = dc[i] + cc
                if 0<=nr<MAXr and 0<=nc<MAXc:
                    if visit[nr][nc] == 0 and maps[nr][nc] != "X":
                        que.append([nr,nc])
                        visit[nr][nc] = 1
                        cnt += int(maps[nr][nc])
                        
        answer.append(cnt)
    
    for i in range(MAXr):
        for j in range(MAXc):
            if maps[i][j] != "X" and visit[i][j] == 0:
                bfs(i,j,int(maps[i][j]))
    
    if not answer:
        return [-1]
    
    answer.sort()
    
    return answer