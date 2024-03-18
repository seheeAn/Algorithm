def solution(park, routes):
    row = len(park)
    col = len(park[0])
    for i in range(row):
        for j in range(col):
            if park[i][j] == "S":
                now_r = i
                now_c = j
                break

    for r in routes:
        new_r = now_r
        new_c = now_c
        d,n = r.split(" ")
        if d == "N":
            new_r += -1 * int(n)
        elif d == "E":
            new_c += int(n)
        elif d == "W":
            new_c += -1 * int(n)
        elif d == "S":
            new_r += int(n)
        
        # 범위 체크
        flag = True
        if 0 <= new_r < row and 0 <= new_c < col:
            # 중간에 장애물 확인
            low_r = min(now_r, new_r)
            high_r = max(now_r, new_r)
            low_c = min(now_c, new_c)
            high_c = max(now_c, new_c)
            for i in range(low_r, high_r+1):
                if park[i][now_c] == "X":
                    flag = False

            for j in range(low_c, high_c+1):
                if park[now_r][j] == "X":
                    flag = False
                    
            if flag == True:
                now_r = new_r
                now_c = new_c
                print(now_r, now_c)
    
    answer = [now_r, now_c]
    return answer
