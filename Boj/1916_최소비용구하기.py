import heapq
N = int(input()) #도시개수
M = int(input()) #버스개수

#메모리 초과로 인접리스트 사용 > 해도 메모리 초과;;;
#해당 지점까지의 현재 cost를 저장하고 이것보다 cost가 작을 경우에만 cost갱신 및 que에 추가
cities = [[] for _ in range(N+1)]
costs = [100000001 for _ in range(N+1)] #100000 * 1000 이 max값

for _ in range(M):
    a, b, c = map(int, input().split())
    cities[a].append([b,c]) #도착지, 비용

start, end = map(int, input().split())

#초기값
que = []
res = 0
heapq.heappush(que, (0, start))
costs[start] = 0

while que:
    cost, city = heapq.heappop(que)
    
    if city == end:
        res = cost
        break

    if costs[city] < cost:
        continue # 밑을 수행하지 않고 다음 iter로 넘어감

    for c in cities[city]:
        next_cost = cost + c[1]
        if next_cost < costs[c[0]]: #해당 지점까지의 cost가 지금까지 저장된 cost보다 작다면
            heapq.heappush(que, (next_cost, c[0]))
            costs[c[0]] = next_cost #힙에 들어갈 때 갱신

print(res)