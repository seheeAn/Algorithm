N, M = map(int, input().split())
houses = []
stores = []

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            houses.append([i,j])
        elif tmp[j] == 2:
            stores.append([i,j])

new_stores = []
res = 100000

def dfs(idx, cnt):
    global res
    if cnt == M:
        score = 0
        for h in range(len(houses)):
            chick = 1000
            for m in range(M):
                dist = abs(houses[h][0]-new_stores[m][0]) + abs(houses[h][1] - new_stores[m][1])
                chick = min(chick , dist)
            score += chick

        res = min(score, res)
        return

    else:
        for i in range(len(stores)):
            new_stores.append(stores[i])
            dfs(i+1, cnt+1)
            new_stores.pop()

dfs(0,0)

print(res)