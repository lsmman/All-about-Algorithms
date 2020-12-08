def solution(answers):
    def is_right(pattern, i, ans):
        return pattern[i % len(pattern)] == ans

    answer = []
    first_p = [1, 2, 3, 4, 5]
    second_p = [2, 1, 2, 3, 2, 4, 2, 5]
    third_p = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0 for _ in range(4)]

    for i, ans in enumerate(answers):
        scores[1] += int(is_right(first_p, i, ans))
        scores[2] += int(is_right(second_p, i, ans))
        scores[3] += int(is_right(third_p, i, ans))

    max_score = max(scores)
    for i, s in enumerate(scores):
        if s == max_score:
            answer.append(i)
    return answer