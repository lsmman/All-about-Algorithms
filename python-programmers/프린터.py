def solution(priorities, location):
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)]

    max_val = max(priorities)

    while True:
        point = queue.pop(0)
        if max_val > point[1]:
            queue.append(point)
        else:
            answer += 1
            if point[0] == location:
                break
            else:
                max_val = max(queue, key=lambda x: x[1])[1]
    return answer