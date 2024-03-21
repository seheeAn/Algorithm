def solution(sequence, k):
    answer = []
    answer_long = len(sequence)
    start=0 
    end=0
    res = sequence[start]
    
    while start <= end:
        if res < k:
            end +=1
            if end == len(sequence):
                break
            else:
                res += sequence[end]
        elif res == k:
            if answer_long > end-start:
                answer = [start, end]
                answer_long = end-start
            res -= sequence[start]
            start += 1
        else:
            res -= sequence[start]
            start += 1
        
    return answer