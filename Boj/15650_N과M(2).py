N, M = map(int, input().split())
li = []

def dfs(start, cnt):
    if cnt == M:
        tmp = ''
        for i in li:
            tmp += str(i) + " "
        print(tmp)
        return
    
    for i in range(start, N+1):
        li.append(i)
        dfs(i+1, cnt+1)
        li.pop()
    
dfs(1, 0)