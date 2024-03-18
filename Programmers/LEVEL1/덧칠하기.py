
def solution(n, m, section):
    answer = 0
    start = -m
    for s in section:
        if s < start + m:
            continue
        else:
            start = s
            answer += 1
            
    return answer