def solution(board):
    answer = 0
    que = []
    N, M = len(board), len(board[0])
    visit = [[0 for _ in range(M+2)] for _ in range(N+2)]
    _board = [["D" for _ in range(M+2)] for _ in range(N+2)]
    for i in range(N):
        for j in range(M):
            _board[i+1][j+1] = board[i][j]
            if _board[i+1][j+1] == "R":
                que.append([i+1,j+1,0])
    
    dr = [0,0,-1,1]
    dc = [-1,1,0,0]
    while que:
        r,c,cnt = que.pop(0)
        # 종료조건
        if _board[r][c] == "G":
            return cnt
        
        for i in range(4):
            nr, nc = r, c
            while True:
                if _board[nr+dr[i]][nc+dc[i]] == "D":
                    break
                else:
                    nr += dr[i]
                    nc += dc[i]
            if visit[nr][nc] == 0:
                visit[nr][nc] = 1
                que.append([nr,nc,cnt+1])
                    
    return -1