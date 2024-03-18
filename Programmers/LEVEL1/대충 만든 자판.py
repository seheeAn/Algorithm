def solution(keymap, targets):
    answer = []
    
    #alphabet list
    max_num = 999
    alphabet = [max_num] * 26
    for k in keymap:
        for i in range(len(k)):
            if alphabet[ord(k[i])-ord("A")] > i+1:
                alphabet[ord(k[i])-ord("A")] = i+1
    
    for t in targets:
        ans = 0
        
        for i in range(len(t)):
            ans+= alphabet[ord(t[i])-ord("A")]
        
        if ans >= 999:
            answer.append(-1)
        else:
            answer.append(ans)
    return answer

# def solution(keymap, targets):
#     answer = []
#     key_dict = {}
    
#     for key in keymap:
#         idx = 1
#         for k in key:
#             if k not in key_dict.keys() or key_dict[k] > idx:
#                 key_dict[k] = idx
#             idx += 1
        
#     for target in targets:
#         tmp = 0
#         for t in target:
#             if t in key_dict.keys():
#                 tmp += key_dict[t]
#             else:
#                 tmp = -1
#                 break
#         answer.append(tmp)
            
#     return answer