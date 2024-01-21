N, M = map(int, input().split())
visit = [0 for _ in range(N+1)]
li = []
def dfs(cnt):
    if cnt == M:
        tmp = ""
        for i in li:
            tmp += str(i)+" "
        print(tmp)
        return

    for i in range(1, N+1):
        if visit[i] == 1:
            continue #다음 for 문
        
        visit[i] = 1
        li.append(i)
        dfs(cnt+1)
        li.pop()
        visit[i] = 0

dfs(0)