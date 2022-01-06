def get_value(unit, pos_x, pos_y):
    if pos_x == 0 and pos_y == 0:
        return 1

    num = ((unit - 1) * 2 + 1) * ((unit - 1) * 2 + 1) + 1

    if pos_x == unit:
        for _y in range(unit - 1, -unit - 1, -1):
            if _y == pos_y:
                return num
            num += 1
    else:
        num += 2 * unit

    if pos_y == -unit:
        for _x in range(unit - 1, -unit - 1, -1):
            if _x == pos_x:
                return num
            num += 1
    else:
        num += 2 * unit

    if pos_x == -unit:
        for _y in range(-unit + 1, unit + 1):
            if _y == pos_y:
                return num
            num += 1
    else:
        num += 2 * unit

    if pos_y == unit:
        for _x in range(-unit + 1, unit + 1):
            if _x == pos_x:
                return num
            num += 1
    else:
        num += 2 * unit

    return num


r1, c1, r2, c2 = map(int, input().split())
MAP = {}
space = 1
print_msg = []

for y in range(r1, r2 + 1):
    for x in range(c1, c2 + 1):
        MAP[(y, x)] = get_value(max(abs(x), abs(y)), x, y)
        space = max(space, len(str(MAP[(y, x)])))

for y in range(r1, r2 + 1):
    for x in range(c1, c2 + 1):
        print_msg.append("%*d " % (space, MAP[(y, x)]))
    print_msg.append("\n")
print("".join(print_msg))
