def solution(myString):
    answer = list(myString.split("x"))
    answer = list(map(lambda x:len(x), answer))
    return answer