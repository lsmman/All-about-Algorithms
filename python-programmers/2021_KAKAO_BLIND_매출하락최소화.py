def solution(sales, links):
    n = len(sales)
    teams = [-1 for _ in range(n)]
    for leader, follower in links:
        l, f = leader - 1, follower - 1
        if teams[l] != -1 and sales[teams[l]] <= sales[f]:
            continue
        teams[l] = f

    teams = [[i, t] for i, t in enumerate(teams) if t]
    staff = [0 for _ in range(n + 1)]
    num_of_teams = len(teams)
    min_val = [int((1 << 31) - 1)]
    sales.append(0)

    def backtracking(idx):
        if idx == num_of_teams:
            min_val[0] = min(staff[-1], min_val[0])
            return
        if staff[-1] >= min_val[0]:
            return
        for t in teams[idx]:
            if not staff[t]:
                staff[-1] += sales[t]
            staff[t] += 1
            backtracking(idx + 1)
            staff[t] -= 1
            if not staff[t]:
                staff[-1] -= sales[t]

    backtracking(0)

    return min_val[0]