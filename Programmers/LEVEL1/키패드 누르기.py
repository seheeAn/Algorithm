def solution(numbers, hand):
    answer = ''
    L = [3,0]
    R = [3,2]
    # num 좌표 = [(num-1)//3 , (num-1)%3]
    left_num = [1,4,7]
    right_num = [3,6,9]
    for num in numbers:
        num_pos = [(num-1)//3, (num-1)%3]
        if num == 0:
            num_pos = [3,1]
        if num in left_num:
            answer += "L"
            L = num_pos
        elif num in right_num:
            answer += "R"
            R = num_pos
        else:
            L_diff = abs(num_pos[0] - L[0]) + abs(num_pos[1]- L[1])
            R_diff = abs(num_pos[0] - R[0]) + abs(num_pos[1]- R[1])
            if L_diff > R_diff or (L_diff == R_diff and hand == "right"):
                answer += "R"
                R = num_pos
            else:
                answer += "L"
                L =  num_pos
            
    return answer