def solution(weights):
    answer = 0
    rate = [1,2,3/2,4/3]
    dicts = dict()
    for w in weights:
        if w in dicts:
            dicts[w] += 1
        else:
            dicts[w] = 1
    
    for w in dicts:
        for r in rate:
            if w*r in dicts:
                if r == 1:
                    answer += (dicts[w] * (dicts[w]-1))/2
                else:
                    answer += (dicts[w] * dicts[w*r])
    
    return answer