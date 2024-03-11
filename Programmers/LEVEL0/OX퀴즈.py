def solution(quiz):
    answer = []
    for q in quiz:
        left, right = q.split('=')
        if "+" in left:
            num1, num2 = left.split("+")
            if int(num1) + int(num2) == int(right):
                answer.append("O")
            else:
                answer.append("X")

        else:
            num1, num2 = left.split(" - ")
            if int(num1) - int(num2) == int(right):
                answer.append("O")
            else:
                answer.append("X")
                
    return answer