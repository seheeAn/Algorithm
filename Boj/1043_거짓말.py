N, M = map(int, input().split())
truth = list(map(int,input().split()))[1:]
party = []
parent = [i for i in range(N+1)]

for _ in range(M):
    tmp = list(map(int,input().split()))[1:]
    party.append(tmp)

def find(x, parent): #부모 찾기
    if x != parent[x]:
        parent[x] = find(parent[x], parent)

    return parent[x]

def union(x, y, parent):
    x = find(x,parent)
    y = find(y,parent)

    # 작은 쪽 부모로 통합
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in truth: #turth 끼리 통합 > 작은쪽으로 통합되므로 진실을 알면 부모가 0이되도록 함
    parent[i] = 0

for i in range(M): #파티를 돌면서 그룹 통합.
    first = party[i][0]
    for person in party[i]:
        if find(first, parent) != find(person, parent):
            union(first, person, parent)

res = 0

for p in party:
    for x in p:
        if find(x, parent) == 0: #truth 그룹과 만나면 
            break
    
    else: #해당 파티에 tuth 그룹이 없으면
        res += 1

print(res)