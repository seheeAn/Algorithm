def solution(rank, attendance):
    answer = 0
    zip_list = []

    for i in range(len(rank)):
        if attendance[i]:
            zip_list.append([i, rank[i]])
            
    zip_list.sort(key=lambda x:x[1])
    
    answer = zip_list[0][0]*10000 + zip_list[1][0]*100 + zip_list[2][0]
    return answer