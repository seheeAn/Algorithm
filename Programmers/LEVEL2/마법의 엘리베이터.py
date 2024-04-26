def solution(storey):
    answer = 0
    # 1. 현재 자리값이 0~4 -> 밑으로 내림
    # 2. 현재 자리값이 6~9 -> 위로 올림
    # 3. 현재 자리값이 5 -> 앞자리가 5 이상이면 올림, 아니면 내림
    
    while storey:
        remain = storey % 10
        
        if 0<=remain<=4:
            answer += remain
            
        elif 6<= remain <= 9:
            answer += 10-remain
            storey += 10

        elif remain == 5:
            if (storey//10) % 10 >= 5:
                storey += 10
            answer += 5
    
        storey = storey//10 #마지막 자리수 날리기
        
    return answer