def get_available_max_distances(term):
    distances = [0]
    moving = distances[0]
    add_ = 0
    odd = True

    while term > moving:
        if odd:
            add_ += 1
        moving += add_
        distances.append(moving)
        odd = not odd

    return distances


def get_move_count(term, distances):
    for i in range(len(distances)):
        if term <= distances[i]:
            return i


terms = []
for case in range(int(input())):
    x, y = map(int, input().split(' '))
    terms.append(y-x)

distances = get_available_max_distances(max(terms))
for term in terms:
    result = get_move_count(term, distances)
    print(result)
