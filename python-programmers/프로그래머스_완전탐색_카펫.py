def solution(brown, yellow):
    sum_of_lines = brown // 2 + 2
    for v in range(int(yellow ** (1 / 2)), 0, -1):
        if yellow % v == 0:
            short, long = v + 2, yellow // v + 2
            if short + long == sum_of_lines:
                return [long, short]
    return []