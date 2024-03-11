def solution(board):
    answer = 0
    n = len(board[0])
    visit = [[0 for _ in range(n)] for _ in range(n)]
    dr = [0, -1, -1, -1, 0, 0, 1, 1, 1]
    dc = [0, -1, 0, 1, -1, 1, -1, 0, 1]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for k in range(9):
                    if 0 <= i+dr[k] <n and 0<= j+dc[k] <n: 
                        if visit[i+dr[k]][j+dc[k]] == 0:
                            answer += 1
                            visit[i+dr[k]][j+dc[k]] = 1
    
    answer = n*n - answer
    
    return answer