def solution(citations):
    max_val = 0
    n = len(citations)

    citations.sort(reverse=True)
    # print(citations)
    for i in range(n):
        # print(citations[i], i+1)
        max_val = max(min(citations[i], i + 1), max_val)

    return max_val