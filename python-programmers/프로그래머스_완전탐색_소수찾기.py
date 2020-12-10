from itertools import permutations


def solution(numbers):
    answer = 0
    n_set = set()
    for i in range(1, len(numbers) + 1):
        permutation = permutations(numbers, i)
        for p in permutation:
            n_set.add(int("".join(p)))

    max_n = max(n_set)
    prime_nums = [True] * (max_n + 1)
    prime_nums[0], prime_nums[1] = False, False
    for i in range(2, int(max_n ** 0.5) + 1):
        for j in range(i + i, max_n + 1, i):
            prime_nums[j] = False

    for n in n_set:
        if prime_nums[n]:
            answer += 1
    return answer


# SET으로 구현한 버전
# 위의 코드 실행속도 1/10

# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)