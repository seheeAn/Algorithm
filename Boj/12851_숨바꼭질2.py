import heapq
MAXNUM = 987654321
N, K = map(int, input().split())
visit = [ MAXNUM for _ in range(100001)]

que = []
heapq.heappush(que, (0,N))
visit[N] = 0

cnt = 0
while que:
    time, pos = heapq.heappop(que)

    if time > visit[pos]:
        continue

    if pos == K:
        cnt += 1
    
    new_pos = [pos+1, pos-1, pos*2]
    for p in new_pos:
        if p >= 0 and p <100001 and visit[p] >= time+1: #같은 것도 포함
            heapq.heappush(que,(time+1, p))
            visit[p] = time+1

print(visit[K])
print(cnt)