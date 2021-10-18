def knapsack(k, items):
    preq_values = [0 for _ in range(k+1)]

    for i, (w, v) in enumerate(items):
        cur_values = [0 for _ in range(k+1)]
        for w_limit in range(1, k+1):
            cur = 0
            if w <= w_limit:
                cur = v + preq_values[w_limit - w]
            cur_values[w_limit] = max(
                preq_values[w_limit],
                cur_values[w_limit-1],
                cur
            )
        preq_values = cur_values
    return preq_values[k]


def main():
    n, k = list(map(int, input().split()))
    items = [list(map(int, input().split())) for _ in range(n)]
    result = knapsack(k, items)
    print(result)


main()

def test():
    cnt = 1

    answer = 14
    k = 7
    items = [[6, 13], [4, 8], [3, 6], [5, 12]]
    result = knapsack(k, items)
    print(cnt, result, result == answer)
    cnt += 1

    answer = 9
    k = 5
    items = [[4, 2], [3, 4], [1, 5]]
    result = knapsack(k, items)
    print(cnt, result, result == answer)
    cnt += 1


test()

"""

10 999
46 306
60 311
33 724
18 342
57 431
49 288
12 686
89 389
82 889
16 289
답:4655


10 11
1 306
1 311
1 724
1 342
1 431
1 288
1 686
1 389
1 889
1 289
답:4655
"""