# 트리의 level 별로 search를 한다.
# bfs 이용 0->1,8 ->2,4,7,9 -> 3,6,10,11
# 총 늑대 수가 적은 노드부터 search 한다
# 0 -> 1 -> 8 -> 7 -> 9 -> 4 ->  이상황에서부터 어케하지...?
# 임시 늑대 수를 저장해 놨다가 양을 만나면 더하기...?
# 0 -> 1 -> 8(1) -> 7 -> 9 -> 2(1) -> 4(1) -> 3(2) -> 6(2) -> 10(1) ->11(1) -> 5

import heapq

def solution(info, edges):
    answer = 0
    tree = [[] for _ in range(len(info))]
    _tree = [[] for _ in range(len(info))]
    for e in edges:
        tree[e[0]].append(e[1])
        _tree[e[1]].append(e[0])
        
    wolfs = 0
    wolfs_li = []
    que = []
    heapq.heappush(que, (0, 0)) #늑대 수, 노드
    
    while que:
        w_cnt, node = heapq.heappop(que)
        
        if info[node] == 0: #양이면
            wolfs += w_cnt
            w_cnt = 0
            answer += 1
        
            check_root_wolf = [node]
            while check_root_wolf:
                n = check_root_wolf.pop(0)
                for idx in _tree[n]:
                    if info[idx] == 1:
                        check_root_wolf.append(idx)
                        if idx not in wolfs_li:
                            wolfs_li.append(idx)
                        else:
                            wolfs -= 1
            # print(wolfs, node, answer)     
            if answer <= wolfs+1 and node!=0:
                answer -= 1
                break
        
        for n_node in tree[node]:
            if info[n_node] == 1:
                heapq.heappush(que, (w_cnt+1, n_node))
            else:
                heapq.heappush(que, (w_cnt, n_node))
            
    return answer