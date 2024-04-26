import heapq

def solution(n, k, enemy):
    answer = 0
    que = []
    
    if k >= len(enemy):
        return len(enemy)
    
    for i, e in enumerate(enemy):
        heapq.heappush(que,e)
        if len(que) > k:
            n -= heapq.heappop(que) # minheap이 기본
            if n < 0:
                break
        answer += 1
    
    return answer