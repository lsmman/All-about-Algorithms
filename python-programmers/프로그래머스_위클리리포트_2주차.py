"""
위클리 리포트 2주차
https://programmers.co.kr/learn/courses/30/lessons/83201

시간 복잡도 : O(n^2)
공간 복잡도 : O(n)
"""

def solution(scores):
    answer = ''
    leng = len(scores)
    scores = list(zip(*scores))
    avg_scores = [0] * leng
    exception = [0] * leng
    
    for i in range(leng):
        s = scores[i][i]
        if (s == max(scores[i]) or \
            s == min(scores[i])) and \
            scores[i].count(s) == 1:
            exception[i] = 1

    for i in range(leng):
        s = sum(scores[i]) - (scores[i][i] * exception[i])
        s /= (leng - exception[i])
        avg_scores[i] = s
    
    for s in avg_scores:
        rank = ''
        if s >= 90:
            rank = 'A'
        elif s >= 80:
            rank = 'B'
        elif s >= 70:
            rank = 'C'
        elif s >= 50:
            rank = 'D'
        else:
            rank = 'F'
        answer += rank
    return answer


import unittest


class test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]), "FBABD")
        self.assertEqual(solution([[50,90],[50,87]], "DA"))
        self.assertEqual(solution([[70,49,90],[68,50,38],[73,31,100]], "CFD"))
	

unittest.main()
