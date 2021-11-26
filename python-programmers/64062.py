import heapq

def solution(stones, k):
    answer = 0
    left = min(stones)
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2
        zero = 0
        for s in stones:
            if s > mid:
                zero = 0
                continue
            zero += 1
            if zero >= k:
                break
        if zero >= k:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    return answer
