def main():
    n = int(input())
    crane = list(map(int, input().split()))
    m = int(input())
    box = list(map(int, input().split()))

    # ⚡ 내림차순 정렬
    crane.sort(reverse = True)
    box.sort(reverse = True)

    time = 0 # 시간
    checked = [False for _ in range(m)] # 박스를 옮겼는지 여부
    count = 0 # 옮긴 박스의 개수 

    positions = [0] * n

    if max(box) > max(crane):
        return -1
    
    for i in range(n):
        c = crane[i]
        for bi in range(positions[i-1], m):
            if c < box[bi]:
                continue
            positions[i] = bi
            break
        else:
            positions[i] = m

    while count < m:
        for i in range(n):
            p = positions[i]
            while p < m:
                if checked[p]:
                    p += 1
                    continue
                checked[p] = True
                count += 1
                p += 1
                break
            positions[i] = p
        time += 1
    return time

result = main()
print(result)

"""
3
6 8 9
5
2 5 2 4 7

2
19 20
7
14 12 16 19 16 1 5

4
23 32 25 28
10
5 27 10 16 24 20 2 32 18 7

10
11 17 5 2 20 7 5 5 20 7
5
18 18 15 15 17
"""