N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for _ in range(3)] for _ in range(N)]

for i in range(3):
    dp[0][i] = arr[0][i]

print(dp[0])

for i in range(1,N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

    print(dp[i])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

 
