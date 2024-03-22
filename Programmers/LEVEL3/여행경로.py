def solution(tickets):
    answer = []
    # 1. 인천공항에서 출발
    # 2. 같은 도시를 여러번 들러도 됨.
    # 3. 모든 티켓을 사용해야함.
    # 4. 가능한 경로가 여러개일 경우 알파벳 순서가 앞서는 경로로..
    
    used = [0] * len(tickets) #티켓 사용 여부
    tickets.sort(key=lambda x:x[1])

    def dfs(route, ticket_cnt):
        nonlocal answer
        if ticket_cnt == len(tickets):
            answer = route
            return True
        
        start = route[-1]

        for i in range(len(tickets)):
            if tickets[i][0] == start and used[i] == 0:
                route.append(tickets[i][1])
                used[i] = 1
                result = dfs(route, ticket_cnt+1)
                if result is True: #탐색 결과가 None이 아닐 때 
                    return result
                route.pop()
                used[i] = 0
        
        return False
    
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN":
            used[i] = 1
            result = dfs(["ICN", tickets[i][1]],1)
            if result is True:
                break  # 경로를 찾은 경우 반복문 종료
            used[i] = 0

    return answer