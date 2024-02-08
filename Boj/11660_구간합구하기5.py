n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range (n)]
dp = [ [0 for _ in range(n+1)] for _ in range(n+1)]

dp[1][1] = arr[0][0]

for i in range(2,n+1):
    dp[1][i] = dp[1][i-1] + arr[0][i-1]
    dp[i][1] = dp[i-1][1] + arr[i-1][0]

for i in range(2, n+1):
    for j in range(2, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for i in range(m):
    res = 0
    x1,y1,x2,y2 = map(int, input().split())
    res = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(res)
