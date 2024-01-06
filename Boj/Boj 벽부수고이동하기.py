from collections import deque
n,m = map(int, input().split())
arr = [list(map(int, input()))for _ in range(n)]
visit = [[[-1]*m for _ in range(n)] for _ in range(2)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    que = deque()
    que.append((0,0,0))
    visit[0][0][0] = 1
    
    while que:
        x, y, cnt = que.popleft()

        if x == n-1 and y == m-1:
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<m and visit[cnt][nx][ny] == -1):
                if arr[nx][ny] == 0:
                    visit[cnt][nx][ny] = visit[cnt][x][y] + 1
                    que.append((nx,ny,cnt))

                ## 다음칸이 벽일 때 벽의 좌표를 que에 넣는다는 생각을 못하고 벽을 통과해서 0에 도착해야한다고만 생각한게 잘못 중 하나였음
                elif cnt == 0 and arr[nx][ny] == 1: #벽 통과 횟수가 0이고, 다음칸이 벽일 때  
                    visit[1][nx][ny] = visit[0][x][y] + 1
                    que.append((nx,ny,1))

        """
        for i in range(n):
            print(visit[i])
        print("\n")
        """

bfs()

answer = [visit[0][n-1][m-1], visit[1][n-1][m-1]]
res = max(answer) if -1 in answer else min(answer)
print(res)
