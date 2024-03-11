def solution(n):
    answer = [[0 for _ in range(n)]for _ in range(n)]
    
    def func(row, col, num, length):
        for i in range(length): #위
            answer[row][col] = num
            col = col+1
            num = num+1
        col-=1
        for i in range(length-1): #오른쪽
            row = row+1
            answer[row][col] = num
            num = num+1
            
        for i in range(length-1): #아래
            col = col-1
            answer[row][col] = num
            num = num+1
        
        for i in range(length-2): # 왼쪽
            row = row-1
            answer[row][col] = num
            num = num+1

        if answer[row][col+1] !=0: # 끝
             return
        elif length-2 == 1:
            answer[row][col+1] = num
            return
        func(row, col+1, num, length-2)
    
    if n == 1:
        answer = [[1]]
        return answer
    
    func(0,0,1,n)
    return answer