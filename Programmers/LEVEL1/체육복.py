def solution(n, lost, reserve):
    answer = 0
    reserve_set = list(set(reserve) -set(lost))
    lost_set = list(set(lost) - set(reserve))  
    answer = n - len(lost_set)
    
    for i in range(len(lost_set)):
        if lost_set[i]-1 in reserve_set:
            reserve_set.remove(lost_set[i]-1)
            answer += 1
        elif lost_set[i]+1 in reserve_set:
            reserve_set.remove(lost_set[i]+1)
            answer += 1
    
    return answer