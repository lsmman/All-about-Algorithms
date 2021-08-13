# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3
# 34분

def solution(numbers, hand):
    answer = ''
    left, right = -1, -1
    dist = [[0 for _ in range(11)] for _ in range(11)]
    hand = hand[0].upper()

    dist[2][5] = dist[5][2] = 1
    dist[2][8] = dist[8][2] = 2
    dist[2][0] = dist[0][2] = 3
    dist[5][8] = dist[8][5] = 1
    dist[5][0] = dist[0][5] = 2
    dist[8][0] = dist[0][8] = 1
    for to in [2, 5, 8, 0]:
        for from_ in [1, 4, 7, -1]:
            dist[from_][to] = dist[from_ + 1][to] + 1
        for from_ in [3, 6, 9]:
            dist[from_][to] = dist[from_ - 1][to] + 1
    for num in numbers:
        if num in [1, 4, 7]:
            left = num
            answer += 'L'
        elif num in [3, 6, 9]:
            right = num
            answer += 'R'
        elif num in [2, 5, 8, 0]:
            l = dist[left][num]
            r = dist[right][num]
            if l > r:
                right = num
                answer += 'R'
            elif l < r:
                left = num
                answer += 'L'
            else:
                if hand == 'L':
                    left = num
                elif hand == 'R':
                    right = num
                answer += hand                
    return answer

result = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
print(result == "LRLLLRLLRRL", result)
result = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
print(result == "LRLLRRLLLRR", result)
result = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
print(result == "LLRLLRLLRL", result)
