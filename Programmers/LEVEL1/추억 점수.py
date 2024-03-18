def solution(name, yearning, photo):
    answer = []
    name_dict = {}
    
    for n,y in zip(name,yearning):
        name_dict[n] = y
    
    for p in photo:
        score = 0
        for man in p:
            if man in name:
                score += name_dict[man]
        answer.append(score)
    
    return answer