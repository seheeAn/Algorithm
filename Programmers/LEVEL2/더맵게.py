import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first >= K:
            break
        new_s = first + second*2
        heapq.heappush(scoville, new_s)
        answer += 1
    
    if len(scoville) == 1:
        if scoville[0] < K:
            return -1
    
    return answer