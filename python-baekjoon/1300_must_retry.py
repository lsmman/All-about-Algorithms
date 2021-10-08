def main():
    n = int(input())
    k = int(input())

    left = 1
    right = k
    answer = 0

    count_smaller = lambda num: sum([min(num // i, n) for i in range(1, n+1)])
    
    while left <= right:
        mid = (left + right) // 2
        result = count_smaller(mid)
        if result >= k:
            answer = mid
            right = mid-1
        else:
            left = mid+1
            
    print(answer)

main()


# def test():
    # count_smaller = lambda num: sum([min(num // i, n) for i in range(1, n+1)])
    # print(count_smaller(1)) # 1
    # print(count_smaller(2)) # 3
    # print(count_smaller(3)) # 5
    # print(count_smaller(4)) # 6
    # print(count_smaller(5)) # 6
    # print(count_smaller(6)) # 8
    # print(count_smaller(7)) # 8
    # print(count_smaller(8)) # 8
    # print(count_smaller(9)) # 9

    # 1 2 3
    # 2 4 6
    # 3 6 9
    # 1 2 2 3 3 4 6 6 9
