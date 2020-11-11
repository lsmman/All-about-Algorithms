# 그룹화하는 방법

def solution(n, computers):
    net = {0:set(i for i in range(n))}
    status = [0] * n
    new = 1
    while net[0]:
        target = net[0].pop()
        conn_min_group = new
        new_group = [target]
        cur, leng = 0, 1
        while True:
            target = new_group[cur]
            for idx, conn in enumerate(computers[target]):
                if not conn:
                    continue
                if not status[idx]:
                    new_group.append(idx)
                    status[idx] = new
                    leng += 1
                else:
                    if status[target] < conn_min_group:
                        conn_min_group = status[idx]
            cur += 1
            if leng is cur:
                break

        if conn_min_group is new:
            net[new] = set(new_group)
            new += 1
        else :
            net[conn_min_group].update(new_group)
            for node in new_group:
                status[node] = conn_min_group

        net[0] = net[0] - set(new_group)

    return len(net.keys()) - 1