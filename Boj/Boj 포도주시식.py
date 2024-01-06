n = int(input())
li = [int(input()) for _ in range(n)]
dp = [0 ]*(n)

if n > 0:
    dp[0] = li[0]
    
if n > 1:
    dp[1] = li[0] + li[1]

if n > 2:
    dp[2] = max(li[0]+li[2], li[1]+li[2], dp[1])

if n > 3:
    for i in range(3, n):
        case1 = dp[i-3] + li[i-1] + li[i]
        case2 = dp[i-2] + li[i]
        case3 = dp[i-1]
        dp[i] = max(case1, case2, case3)

print(dp[n-1])