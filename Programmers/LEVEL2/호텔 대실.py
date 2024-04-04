def solution(book_time):
    answer = 1
    
    #시간 변환
    book_list = []
    for book in book_time:
        s_hh, s_mm = map(int, book[0].split(":"))
        e_hh, e_mm = map(int, book[1].split(":"))
        start = s_hh*60 + s_mm
        end = e_hh*60 + e_mm
        book_list.append([start, end])
    
    book_list.sort()
    room_list = [0]
    for book in book_list:
        start, end = book
        flag = False
        for i in range(len(room_list)):
            if room_list[i] <= start:
                room_list[i] = end+10
                break
                
        else: # break를 안하고 끝까지 for문이 완료되면 실행
            answer += 1
            room_list.append(end+10)
        
    return answer

### 누적합으로 풀기 ###
def solution(book_time):
    time_list = [0 for _ in range(24*60 + 10)]
    #시간 변환
    book_list = []
    for book in book_time:
        s_hh, s_mm = map(int, book[0].split(":"))
        e_hh, e_mm = map(int, book[1].split(":"))
        start = s_hh*60 + s_mm
        end = e_hh*60 + e_mm + 10
        time_list[start] += 1
        time_list[end] -= 1
    
    num = 0
    for i, time in enumerate(time_list):
        num += time
        time_list[i] = num
        
    return max(time_list)