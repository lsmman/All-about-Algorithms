# 수식 최적화
# https://programmers.co.kr/learn/courses/30/lessons/67257?language=python3
# 32분

from itertools import permutations

def calc(num1, num2, p):
    if p == '+':
        return num1 + num2
    elif p == '-':
        return num1 - num2
    else:
        return num1 * num2

def solution(expression):
    loc = 0
    answer = 0
    elements = []

    for i, e in enumerate(expression):
        if e in "+-*":
            elements.append(int(expression[loc:i]))
            elements.append(e)
            loc = i+1
    elements.append(int(expression[loc:]))
    
    for permutation in permutations("+-*"):
        bucket = elements[:]
        for p in permutation:
            cur = []
            i = 0
            leng = len(bucket)
            while i < leng:
                b = bucket[i]
                if b == p:
                    num1 = cur.pop()
                    num2 = bucket[i+1]
                    cur.append(calc(num1, num2, p))
                    i = i + 2
                else:
                    cur.append(b)
                    i = i + 1
            bucket = cur
        answer = max(answer, abs(bucket[0]))
    
    return answer


result = solution("100-200*300-500+20")
print(result == 60420, result)
result = solution("50*6-3*2")
print(result == 300, result)