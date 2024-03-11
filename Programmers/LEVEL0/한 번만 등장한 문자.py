def solution(s):
    answer = ''
    tmp = []
    is_dup = []
    for c in s:
        if c not in is_dup and c not in tmp:
            tmp.append(c)
        elif c in tmp and c not in is_dup:
            is_dup.append(c)
    
    tmp.sort()
    for t in tmp:
        if t not in is_dup:
            answer+=t
    
    return answer