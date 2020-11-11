import math

"""
* O(n^2)
못난 나의 완전탐색 구현
"""

def Find_the_farthest_distance(Arrow):
    max_distance = 0
    length = len(Arrow)
    for p1 in range(length-1):
        for p2 in range(p1, length):
            distance_x = Arrow[p1][0] - Arrow[p2][0]
            distance_y = Arrow[p1][1] - Arrow[p2][1]
            distance_square = (distance_x * distance_x + distance_y * distance_y)
            if (max_distance < distance_square):
                max_distance = distance_square
    print(math.sqrt(max_distance))

if __name__ == "__main__":
    # input value assigned
    num_of_arrow = int(input())
    Arrow = [[0, 0] for _ in range(num_of_arrow)]
    for idx in range(num_of_arrow):
        raw_input = input().split(" ")
        Arrow[idx] = [int(raw_input[0]), int(raw_input[1])]
    
    Find_the_farthest_distance(Arrow)


"""
* Example input and output

case 1
2
2 2
-1 -2

5.0

case 2
5
-4 1
-100 0
0 4
2 -3
2 300

316.86590223

"""