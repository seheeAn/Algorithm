def solution(array):
    answer = 0
    number = [0 for _ in range(1001)]
    
    for arr in array:
        number[arr] += 1
    
    # max_num = max(number) 
    # answer = number.index(max_num)
    # number[answer] = 0
    
    # if max(number) == max_num:
    #     return -1

    if number.count(max(number)) > 1: # count;;
        return -1
    answer = number.index(max(number))
    return answer