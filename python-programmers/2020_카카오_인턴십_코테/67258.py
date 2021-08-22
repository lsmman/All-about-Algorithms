# 보석 쇼핑
# https://programmers.co.kr/learn/courses/30/lessons/67258?language=python3
# 34분..

def solution(gems):
    answer = [1, len(gems)]
    nums = []
    name2idx = {}
    idx = 0
    for g in gems:
        if g not in name2idx:
            name2idx[g] = idx
            idx += 1
        nums.append(name2idx[g])
    unique = idx
    leng = len(nums) 

    period_leng = 2 * leng
    for srt in range(leng - unique):
        visit = [0] * unique
        cnt = 0
        for end in range(srt, min(srt+period_leng-1, leng)):
            if visit[nums[end]] == 0:
                cnt += 1
            visit[nums[end]] += 1
            if cnt == unique:
                period_leng = end-srt+1
                answer = [srt+1, end+1]
                break
        
    return answer

result = solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
print(result == [3, 7], result)
result = solution(["AA", "AB", "AC", "AA", "AC"])
print(result == [1, 3], result)
result = solution(["XYZ", "XYZ", "XYZ"])
print(result == [1, 1], result)
result = solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
print(result == [1, 5], result)