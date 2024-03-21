def solution(targets):
    answer = 0
    targets.sort(key=lambda x:x[1])
    end = -1
    for target in targets:
        if end <= target[0]:
            answer += 1
            end = target[1]
    
    return answer