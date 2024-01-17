import heapq
MAXNUM = 100001
N, K = map(int, input().split())
dp = [MAXNUM for _ in range(MAXNUM)]

que = []
dp[N] = 0
que.append([0,N]) #time, pos

while que:
    time, pos = heapq.heappop(que)
    
    if dp[pos] < time:
        continue #다음 iter
    
    if N < K and pos < K:
        if pos*2 < MAXNUM and time < dp[pos*2] :
            dp[pos*2] = time
            heapq.heappush(que, [time, pos*2])
        if pos+1 < MAXNUM and time+1 < dp[pos+1]:
            dp[pos+1] = time+1
            heapq.heappush(que, [time+1, pos+1])

    if pos-1 >= 0  and time+1 < dp[pos-1]:
        dp[pos-1] = time+1
        heapq.heappush(que, [time+1, pos-1])

print(dp[K])

