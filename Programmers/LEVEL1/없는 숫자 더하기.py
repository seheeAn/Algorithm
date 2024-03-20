def solution(numbers):
    answer = 0
    num_li = [0,1,2,3,4,5,6,7,8,9]
    
    for num in num_li:
        if num not in numbers:
            answer+=num
    return answer


"""
도랐다...
def solution(numbers):
    answer = 45 - sum(numbers)
    return answer

""" 
