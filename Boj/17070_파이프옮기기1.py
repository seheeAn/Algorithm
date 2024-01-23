N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
#가로>대각선 / 세로>대각선 / 대각선>가로 / 대각선>세로 / 대각선>대각선

cnt = 0
def dfs(x,y,r):
    global cnt
    if x == N-1 and y == N-1:
        cnt += 1
        return
    
    if r == 0 or r == 1: #가로 이동
        if y+1 < N and not arr[x][y+1]:
            dfs(x, y+1, 0)
    
    if r == 2 or r == 1:
        if x+1 < N and not arr[x+1][y]: #세로이동
            dfs(x+1, y, 2)
    
    if r==0 or r==1 or r==2:
        if x+1 < N and y+1 < N:
         if not arr[x+1][y] and not arr[x][y+1] and not arr[x+1][y+1]: #대각선이동
            dfs(x+1, y+1, 1)

dfs(0,1,0)
print(cnt)