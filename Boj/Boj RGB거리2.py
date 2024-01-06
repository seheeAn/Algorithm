
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
INF = 9999999
ans = INF

#첫번째 값을 고정 (마지막과 비교 위함)
for i in range(3): 
    dp[0][0] = dp[0][1] = dp[0][2] = INF #초기화
    dp[0][i] = arr[0][i] #첫번째 색 고정

    for j in range(1, n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) +arr[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) +arr[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) +arr[j][2]

    for k in range(3): #마지막 색과 첫번째 색 비교
        if k != i:
            ans = min(ans, dp[n-1][k])

print(ans)