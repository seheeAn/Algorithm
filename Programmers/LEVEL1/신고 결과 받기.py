def solution(id_list, report, k):
    answer = []
    
    #초기화
    report_people_dict = {} #신고자 : 신고당한 사람
    reported_cnt_dict = {} #신고당한 사람 : count
    for id in id_list:
        report_people_dict[id] = []
        reported_cnt_dict[id] = 0
    
    for r in report:
        tmp = r.split(" ")
        if tmp[1] not in report_people_dict[tmp[0]]:
            report_people_dict[tmp[0]].append(tmp[1])
            reported_cnt_dict[tmp[1]] += 1
    
    for id in id_list:
        cnt = 0
        for people in report_people_dict[id]:
            if reported_cnt_dict[people] >= k:
                cnt += 1
    
        answer.append(cnt)
    return answer
