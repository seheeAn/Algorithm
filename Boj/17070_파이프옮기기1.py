N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
move = [[0,1],[1,1],[1,0]] # 오른쪽, 대각선, 아래
que = [[0,1,0]] #x,y,rotate(0,1,2) 가로,대각선,세로

#가로>대각선 / 세로>대각선 / 대각선>가로 / 대각선>세로 / 대각선>대각선

cnt = 0
while que:
    x, y, r = que.pop(0)
    
    if x == N-1 and y == N-1:
        cnt += 1
    
    for i in range(3):
        
        if r == 0 and i == 2: #가로일때 세로 이동이면
            continue #해당 iter 실행 x
        elif r == 2 and i == 0: #세로일때 가로 이동이면
            continue #해당 iter 실행 x

        new_x = x + move[i][0]
        new_y = y + move[i][1]
        new_r = i

        if new_x < N and new_y < N: #범위 확인
            if not (i == 1 and (arr[new_x][y] == 1 or arr[x][new_y] == 1)): #대각선일 경우 위, 옆 체크
                if arr[new_x][new_y] == 0: #벽이 아니면
                    que.append([new_x,new_y,new_r])

print(cnt)