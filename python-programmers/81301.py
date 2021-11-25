# 2021 카카오 채용연계 인턴쉽


def solution(s):
    answer = ""
    word2info = {"ze":(0, 4), "on":(1, 3), "tw":(2, 3), "th":(3, 5), "fo":(4, 4), "fi":(5, 4), "si":(6, 3), "se":(7, 5), "ei":(8, 5), "ni":(9, 4)}
    
    i = 0
    length = len(s)
    while i < length:
        if s[i].isdigit():
            answer += s[i]
            i += 1
        else:
            num, leng = word2info[s[i:i+2]]
            answer += str(num)
            i += leng
            
    return int(answer)