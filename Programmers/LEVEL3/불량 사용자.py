def solution(user_id, banned_id):
    answer = 0
    match = [[] for _ in range(len(banned_id))]
    
    # 1. banned_id 마다 해당되는 id check
    for idx,ban in enumerate(banned_id):
        for user in user_id:
            if len(user) == len(ban):
                flag = True
                for i,j in zip(ban, user):
                    if i == "*" or i == j:
                        pass
                    else:
                        flag = False
                if flag:
                    match[idx].append(user)
            else:
                continue # 다음 loop

    # 2.dfs로 탐색
    # set으로 마지막에 중복제거
    res = []
    def dfs(idx, li):
        nonlocal answer
        if idx == len(match):
            if set(li) not in res:
                res.append(set(li))
                answer += 1
            return
        for user in match[idx]:
            if user not in li:
                li.append(user)
                dfs(idx+1, li)
                li.pop()
        return 
    
    dfs(0, [])
    
    return answer