from collections import Counter


def get_the_most_frequency_number(arr):
    # 가장 빈도 높은 수 찾기
    max_k, max_v = 0, 0
    for k, v in Counter(arr).items():
        if v > max_v:
            max_k, max_v = k, v
        elif v == max_v:
            max_k = max(max_k, k)
    return max_k


def solution():
    loop = int(input())
    for _ in range(loop):
        t = int(input())
        arr = list(map(int, input().split()))
        ans = get_the_most_frequency_number(arr)
        print("#{} {}".format(t, ans))


if __name__ == "__main__":
    solution()