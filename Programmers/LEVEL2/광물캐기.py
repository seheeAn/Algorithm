def solution(picks, minerals):
    answer = 25 * len(minerals)
    # picks = [dia, iron, stone]
    tire_list = [[1,1,1],[5,1,1],[25,5,1]]
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            minerals[i] = 0
        elif minerals[i] == "iron":
            minerals[i] = 1
        else:
            minerals[i] = 2

    # dfs
    def dfs(idx, tired, pick_li):
        nonlocal answer
        if idx == len(minerals) or pick_li == [0, 0, 0]: # 종료 조건
            if answer > tired:
                answer = tired
                return
        
        for i in range(len(pick_li)):
            if pick_li[i]: # 0이 아니면
                pick_li[i] -= 1
                # 캐기
                cnt = 0
                n_idx = idx
                n_tired = tired
                while n_idx < len(minerals):
                    cnt += 1
                    n_tired += tire_list[i][minerals[n_idx]]
                    n_idx += 1
                    if cnt == 5:
                        break
                dfs(n_idx, n_tired, pick_li)
                pick_li[i] += 1
        return
    
    dfs(0, 0, picks)
    
    return answer