def solution(numbers, target):
    answer = 0
    
    def dfs(idx, tmp):
        nonlocal answer
        if idx == len(numbers):
            if tmp == target:
                answer +=1
            return
        
        dfs(idx+1, tmp+numbers[idx])
        dfs(idx+1, tmp-numbers[idx])
        
    dfs(0,0)
    return answer