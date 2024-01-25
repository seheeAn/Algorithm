N, M = map(int,input().split())
li = []

def dfs(num, cnt):
    if cnt == M:
        tmp = ''
        for n in li:
            tmp += str(n)+" "
        print(tmp)
        return
    
    for i in range(num, N+1):
        li.append(i)
        dfs(i, cnt+1)
        li.pop()

dfs(1, 0)