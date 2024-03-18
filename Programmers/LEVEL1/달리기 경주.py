def solution(players, callings):
    #list.index()가 시간이 오래 걸림... dict로 찾는게 더 빠름
    idx_dict = {}
    for i, p in enumerate(players):
        idx_dict[p] = i
        
    for c in callings:
        idx = idx_dict[c]
        idx_dict[c] -= 1
        front = players[idx-1]
        idx_dict[front] += 1
        
        players[idx-1] = c
        players[idx] = front
        
    return players
