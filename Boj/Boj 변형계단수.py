n = int(input())
dp = [[[0 for _ in range(5)] for _ in range(10)] for _ in range(n)]
mod = 1000000007
#0=- 1=1증가 2=2증가 3=1하락 4=2하락
for i in range(0,10):
    dp[0][i][0] = 1

for i in range(1,n):
    #하락
    for j in range(0,9):
        dp[i][j][3] = (dp[i-1][j+1][0] + dp[i-1][j+1][1] + dp[i-1][j+1][2]) % mod
        dp[i][j][4] = dp[i-1][j+1][3]
    
    #상승
    for j in range(1,10):
        dp[i][j][1] = (dp[i-1][j-1][0] + dp[i-1][j-1][3] + dp[i-1][j-1][4]) %mod
        dp[i][j][2] = dp[i-1][j-1][1]

res = 0
for i in range(0,10):
    res += sum(dp[-1][i])
    res %= mod

print(res)
