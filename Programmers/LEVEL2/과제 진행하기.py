def solution(plans):
    answer = []
    for plan in plans:
        hh, mm = plan[1].split(":")
        plan[1] = int(hh) * 60 + int(mm) # 시작 시간
        plan[2] = plan[1] + int(plan[2]) # 종료 시간
    plans.sort(key=lambda x:x[1])

    time = plans[0][1] #첫번째 과제 시작 시간
    temp = [] #stack. 최근 멈춘 과제부터 꺼내와야함
    ptr = 0
    while len(answer) < len(plans):
        if ptr < len(plans)-1:
            if plans[ptr][2] < plans[ptr+1][1]: # 시간이 중간에 뜨면
                answer.append(plans[ptr][0]) #현재 과제 완료
                time = plans[ptr][2]
                while temp: #남은 과제 진행
                    task = temp.pop()
                    time += task[1]
                    if time <= plans[ptr+1][1]:
                        answer.append(task[0])
                    else:
                        temp.append([task[0], time - plans[ptr+1][1]]) #남은시간 갱신
                        break
                ptr += 1

            elif plans[ptr][2] == plans[ptr+1][1]: # 시간이 같음
                time = plans[ptr+1][1]
                answer.append(plans[ptr][0])
                ptr += 1
            else:
                remain_time = plans[ptr][2] - plans[ptr+1][1]
                temp.append([plans[ptr][0], remain_time])
                ptr += 1
        else:
            answer.append(plans[ptr][0])
            while temp:
                task = temp.pop()
                answer.append(task[0])