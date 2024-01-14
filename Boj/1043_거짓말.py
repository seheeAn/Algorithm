N, M = map(int, input().split())
people = [0 for _ in range(N+1)]
tmp = list(map(int,input().split()))
res = 0

for i in range(tmp[0]):
    people[tmp[i+1]] = 1 #진실을 알면 1

def dfs(party_idx, people_li, lie_cnt):
    global res

    if party_idx == M:
        res = max(lie_cnt, res) #최댓값 갱신
        return 
    
    participants = arr[party_idx]
    know_lie = False
    know_truth = False
    new_people_li = people_li.copy()

    for idx in participants:
        if people_li[idx] == 1:
            know_truth = True
        if people_li[idx] == -1:
            know_lie = True

    if know_lie and know_truth: #모순발생 > 해당 루트 제거
        return

    elif know_lie: #거짓말만 알 때 
        for idx in participants:
            new_people_li[idx] = -1
        dfs(party_idx+1, new_people_li, lie_cnt+1)
    
    elif know_truth: #진실만 알 때 
        for idx in participants:
            new_people_li[idx] = 1
        dfs(party_idx+1, new_people_li, lie_cnt)
    
    else: #둘다 모를때
        for idx in participants:
            new_people_li[idx] = 1 #진실 말하기
        dfs(party_idx+1, new_people_li, lie_cnt)

        new_people_li = people_li.copy()
        
        for idx in participants:
            new_people_li[idx] = -1 #거짓 말하기
        dfs(party_idx+1, new_people_li, lie_cnt+1)

arr = []
for i in range(M):
    tmp = list(map(int, input().split()))
    arr.append(tmp[1:])
            
dfs(0, people, 0)

print(res)