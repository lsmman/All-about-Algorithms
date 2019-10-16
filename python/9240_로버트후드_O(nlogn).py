"""
* Study until having yours

Brief explain about convex hull and graham's scan (https://www.crocus.co.kr/1288)
Concept about convex hull and Rotating calipers(https://www.slideshare.net/ssuser88a8b3/2-57761427)
CCW implement on graham's scan(https://www.acmicpc.net/blog/view/27)
"""
import math

def comp(p1, p2):
    if (p1.q * p2.p != p1.p * p2.q):
        return p1.q * p2.p < p1.p * p2.q
    if (p1.y != p2.y):
        return p1.y < p2.y
    else :
        return p1.x < p2.x

class point(object):
    x, y = 0, 0
    p, q = 0, 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_val(self):
        print(self.x, self.y, self.p, self.q)

    def __lt__(self, other):
        return comp(self, other)
    def __gt__(self, other):
        return comp(self, other)
    # def __eq__(self, other):
    #     return comp(self, other) == 0
    # def __le__(self, other):
    #     return comp(self, other) <= 0
    # def __ge__(self, other):
    #     return comp(self, other) >= 0

class Stack(list):
    push = list.append


    def size(self):
        return len(self)
    
    def peek(self):
        return self[-1]

"""
# function ccw(point[3][2]))

점 3개를 이은 선분의 방향성

시계 방향, 일직선, 반시계 방향이 존재할 수 있다.
세점 사이의 관계는 삼각형의 면적을 구하는 방법으로 구할 수 있다.
세 점의 x, y 좌표를 벡터 행렬로 구할 수 있다.
S =  1/2 * | x1 y1 1 |
           | x2 y2 1 |
           | x3 y3 1 |
  = (x2 - x1)(y3 - y1) - (y2 - y1)(x3 - x1)

S > 0 : 반시계 방향
S = 0 : 일직선
S < 0 : 시계 방향
"""

def cmp(a, b):
    return (a > b) - (a < b)
        
def ccw(p1, p2, p3):
    left = p1.x * p2.y + p2.x * p3.y + p3.x * p1.y
    right = p1.y * p2.x + p2.y * p3.x - p3.y * p1.x
    half_S = left - right

    # S > 0 : 반시계 방향
    # S = 0 : 일직선
    # S < 0 : 시계 방향

    return cmp(half_S, 0)


def max_distance_by_comparing_square_sum(Arrow):
    max_distance = 0
    length = len(Arrow)
    for p1 in range(length-1):
        for p2 in range(p1, length):
            distance_x = Arrow[p1].x - Arrow[p2].x
            distance_y = Arrow[p1].y - Arrow[p2].y
            distance_square = (distance_x * distance_x + distance_y * distance_y)
            if (max_distance < distance_square):
                max_distance = distance_square
    print(math.sqrt(max_distance))


def Find_the_farthest_distance(points):
    length = len(points)

    # y좌표, x좌표가 작은 순으로 정렬
    points.sort()
    
    # 기준점 0번째 points의 (x, y)로부터 각각 상대위치 계산
    std_x = points[0].x
    std_y = points[0].y

    for p in points:
        p.p = p.x - std_x
        p.q = p.y - std_y
    
    # p, q의 각도 cos값을 이용하여 sort
    # 반시계 방향으로 정렬
    points.sort()

    # stack s about graham's scan 선언
    s = Stack()
    s.push(0)
    s.push(1)

    next_num = 2

    while (next_num < length):
        while (s.size() >= 2):
            second = s.peek()
            s.pop()
            first = s.peek()

            if (ccw(points[first], points[second], points[next_num]) > 0):
                s.push(second)
                break
        s.push(next_num)
        next_num = next_num+1

    Arrow = []
    for idx in s:
        Arrow.append(points[idx])
    max_distance_by_comparing_square_sum(Arrow)


if __name__ == "__main__":
    num_of_arrow = int(input())
    Arrow = []
    for idx in range(num_of_arrow):
        raw_input = input().split(" ")
        Arrow.append(point(int(raw_input[0]), int(raw_input[1])))
    
    Find_the_farthest_distance(Arrow)


""" 
5
-4 1
-100 0
0 4
2 300
2 -3

ans : 316.86590223626143
"""