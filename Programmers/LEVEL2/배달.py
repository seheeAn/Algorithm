import heapq

def solution(N, road, K):
    answer = 0
    visit = [500001] * (N+1)
    graph = [[] for _ in range(N+1)]
    
    for r in road:
        graph[r[0]].append([r[2],r[1]]) #거리, 도착지
        graph[r[1]].append([r[2],r[0]])
    
    que = []
    heapq.heappush(que, [0,1])
    visit[1] = 0 #초기화 주의...
    while que:
        time,spot = heapq.heappop(que)
        if visit[spot] < time:
            continue
        for item in graph[spot]:
            n_time = time+item[0]
            n_spot = item[1]
            if visit[n_spot] > n_time:
                visit[n_spot] = n_time
                heapq.heappush(que, [n_time, n_spot])
    
    for v in visit:
        if v <= K:
            answer += 1
    
    return answer