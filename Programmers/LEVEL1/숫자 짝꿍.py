def solution(X, Y):
    answer = ''
    X_li = [0] * 10
    Y_li = [0] * 10
    
    for x in X:
        X_li[int(x)] += 1
    for y in Y:
        Y_li[int(y)] += 1
    
    for i in range(9,-1,-1):
        iter_num = min(X_li[i], Y_li[i])
        answer+=str(i)*iter_num
    
    if answer == "":
        return "-1"
    elif answer[0] == "0":
        return "0"
    
    return answer