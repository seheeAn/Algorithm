def solution(a, b, g, s, w, t):
    answer = 2 * 10**9 * 2 * 10**5 #a=10**9, b=10**9, t=10**5, w=1 
    start = 0
    end =  2 * 10**9 * 2 * 10**5
    
    while start <= end:
        mid = (start+end) // 2
        gold = 0
        silver = 0
        total = 0
        for i in range(len(t)):
            move = mid // (2*t[i])
            if mid % (2*t[i]) >= t[i]:
                move += 1 #편도로 한 번 가능
            
            _gold = min(g[i], move*w[i])
            _silver = min(s[i], move*w[i])
            _total = min(_gold+_silver, move*w[i])
            
            gold += _gold
            silver += _silver
            total += _total
        
        if a <= gold and b <= silver and a+b <= total:
            end = mid-1
        else:
            start = mid+1
        
    answer = start 
    
    return answer