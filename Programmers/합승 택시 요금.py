import heapq

def solution(n, s, a, b, fares):
    answer = 0
    #왕복 구간이 있어도 최소일 수 있음
    share = 1000001 * 200 
    a_fare = 0 
    b_fare = 0
    
    #간선, visit 배열 초기화
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for f in fares:
        d, e, c = f
        graph[d][e] = c
        graph[e][d] = c

    def dijkstra(start, end):
        que = []
        visit = [1000001 * 200 for _ in range(n+1)]
        visit[start] = 0
        heapq.heappush(que, (0, start))
                
        while que:
            c, pos = heapq.heappop(que)
            if pos == end:
                return c
            
            if visit[pos] < c: 
                continue
                
            for i in range(1, len(graph[pos])):
                n_cost = graph[pos][i]
                if n_cost != 0:
                    if visit[i] > c+n_cost:
                        heapq.heappush(que, (c+n_cost, i))
                        visit[i] = c+n_cost
        
        return visit[end] #못찾은 경우
                        
    #a까지의 최소요금
    a_fare = dijkstra(s, a)
    print(a_fare)
    #b까지의 최소요금
    b_fare = dijkstra(s, b)
    print(b_fare)
    #a+b 합승시 최소요금
    for i in range(1, n+1):
        if i != s:
            share = min(share, dijkstra(s,i) + dijkstra(i,a) + dijkstra(i,b)) 
            #각 지점까지의 최소값 + 해당 지점에서 a, b까지의 최소값
    
    answer = min(share, a_fare+b_fare)
    
    return answer