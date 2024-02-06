N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]

dr = [-1, 0, 0, 1] #위, 왼, 오, 아
dc = [0, -1, 1, 0]

def find_fish(row, col, time, cnt, size):
    que = [(row, col, time)]
    while que:
        r, c, t = que.pop(0)
        visit[r][c] = t

        for i in range(4):
            n_r = r + dr[i]
            n_c = c + dc[i]

            if 0<=n_r<N and 0<=n_c<N and visit[n_r][n_c] == 0:
                if (arr[n_r][n_c] == 0 or arr[n_r][n_c] == size):
                    visit[n_r][n_c] = t+1
                    que.append((n_r,n_c,t+1))

                elif (arr[n_r][n_c] < size):
                    tmp_r = n_r
                    tmp_c = n_c
                    for _r, _c, _t in que:
                        if _t > t:
                            break
                        for i in range(4):
                            nn_r = _r+dr[i]
                            nn_c = _c+dc[i]

                            if 0<=nn_r<N and 0<=nn_c<N and visit[nn_r][nn_c] == 0:
                                if arr[nn_r][nn_c] < size and arr[nn_r][nn_c] != 0 :
                                    if nn_r < tmp_r:
                                        tmp_r = nn_r
                                        tmp_c = nn_c
                                    elif nn_r == tmp_r:
                                        if nn_c < tmp_c:
                                            tmp_c = nn_c

                    visit[tmp_r][tmp_c] = t+1
                    cnt += 1
                    if cnt == size:
                        size += 1
                        cnt = 0 
                    arr[tmp_r][tmp_c] = 0
                    return tmp_r, tmp_c, cnt, size, t+1
    
    return r, c, cnt, size, time

start_r = 0
start_c = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            start_r = i
            start_c = j
            arr[i][j] = 0
            break

cnt = 0
size = 2
res = 0
time = 0

while True:

    #visit 배열 초기화
    for i in range(N):
        for j in range(N):
            visit[i][j] = 0

    n_r, n_c, _cnt, _size, _time = find_fish(start_r, start_c, time, cnt, size)

    if _cnt == cnt and _size == size:
        res = _time
        break
    
    cnt = _cnt
    size = _size
    time = _time
    start_r = n_r
    start_c = n_c

print(res)
