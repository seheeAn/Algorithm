def solution(wallpaper):
    row = len(wallpaper)
    col = len(wallpaper[0])
    
    min_r = row
    max_r = -1
    min_c = col
    max_c = -1
    
    for i in range(row):
        for j in range(col):
            if wallpaper[i][j] == "#":
                if i > max_r:
                    max_r = i
                if i < min_r:
                    min_r = i
                if j > max_c:
                    max_c = j
                if j < min_c:
                    min_c = j
    
    answer = [min_r, min_c, max_r+1, max_c+1]
    
    return answer