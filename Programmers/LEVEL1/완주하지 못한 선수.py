def solution(participant, completion):
    answer = ''
    participant = sorted(participant)
    completion = sorted(completion)
    
    point = 0
    
    while point < len(completion):
        if participant[point] != completion[point]:
            return participant[point]
        else:
            point += 1
    
    return participant[point]