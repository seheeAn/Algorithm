N, K = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)] #무게, 가치

dp = [[0 for _ in range(N)] for _ in range(K+1)]

for weight in range(1, K+1):
    for i, item in enumerate(arr):
        if item[0] > weight:
            if i == 0:
                dp[weight][i] = 0
            else:
                dp[weight][i] = dp[weight][i-1]
        
        else:
            if i == 0:
                dp[weight][i] =  item[1]
            else:
                dp[weight][i] = max(dp[weight-item[0]][i-1]+ item[1], dp[weight][i-1])
            # 현재 가능 무게에서 아이템 무게를 뺀 무게에서의 최대가치 + 현재 아이템 가치
            # 지금 아이템을 담지 않고 이전 아이템까지 고려했을 때의 최대 가치

print(dp[K][N-1])