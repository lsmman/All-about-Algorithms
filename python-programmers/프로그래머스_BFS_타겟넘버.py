from itertools import accumulate


def solution(numbers, target):
    numbers.sort()
    avail = list(accumulate(numbers)) + [0]

    def dfs(cur, index):
        if index < 0:
            if cur == 0:
                avail[-1] += 1
            return
        elif not (-avail[index] <= cur <= avail[index]):
            return
        dfs(cur + numbers[index], index - 1)
        dfs(cur - numbers[index], index - 1)

    dfs(target, len(numbers) - 1)
    return avail[-1]