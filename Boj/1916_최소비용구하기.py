import heapq

N = int(input()) #도시개수
M = int(input()) #버스개수
buses = [list(map(int, input().split())) for _ in range(M)]
#출발도시, 도착도시, 버스비용

cities = [[100000 for _ in range(N+1)] for _ in range(N+1)]
visit = [0 for _ in range(N+1)]

for bus in buses:
    cities[bus[0]][bus[1]] = min(bus[2], cities[bus[0]][bus[1]])

start, end = map(int, input().split())

que = []
res = 0 #max 값

#초기화
for i in range(1, N+1):
    heapq.heappush(que, (cities[start][i], i))#비용, 도착지 (비용을 기준으로 min heap)


while(que):
    cost, city = heapq.heappop(que)
    visit[city] = 1

    if city == end:
        res = cost
        break
    
    else:
        for i in range(1, N+1):
            if visit[i] == 0: #방문한 적 없으면
                heapq.heappush(que, (cost + cities[city][i], i))

print(res)