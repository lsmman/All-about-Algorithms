# 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
# 34분..
# 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
# 
def solution(gems):
    gems_length = len(gems)
    names2count = {g:0 for g in set(gems)}
    n = len(names2count)
    cnt = 0
    answer = (gems_length, 0, gems_length-1)
    
    srt = 0
    end = -1
    while srt < gems_length:
        for i in range(end+1, gems_length):            
            if cnt == n:
                break
                
            if not names2count[gems[i]]:
                cnt += 1
            names2count[gems[i]] += 1
            
            end = i
        
        if cnt == n and answer[0] > (end-srt):
            answer = (end-srt, srt, end)
            if answer[0]+1 == n:
                break
        
        names2count[gems[srt]] -= 1
        if not names2count[gems[srt]]:
            cnt -= 1
        srt += 1
        
    return [answer[1]+1, answer[2]+1]
    
result = solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
print(result == [3, 7], result)
result = solution(["AA", "AB", "AC", "AA", "AC"])
print(result == [1, 3], result)
result = solution(["XYZ", "XYZ", "XYZ"])
print(result == [1, 1], result)
result = solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
print(result == [1, 5], result)