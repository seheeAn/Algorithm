def solution(survey, choices):
    answer = ''
    mbti_dict = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for sur, num in zip(survey, choices):
        disagree = sur[0]
        agree = sur[1]
        if num < 4:
            mbti_dict[disagree] += 4-num
        elif num > 4:
            mbti_dict[agree] += num-4
    
    answer = answer+"R" if mbti_dict["R"] >= mbti_dict["T"] else answer+"T"
    answer = answer+"C" if mbti_dict["C"] >= mbti_dict["F"] else answer+"F"    
    answer = answer+"J" if mbti_dict["J"] >= mbti_dict["M"] else answer+"M"
    answer = answer+"A" if mbti_dict["A"] >= mbti_dict["N"] else answer+"N"
        
    return answer