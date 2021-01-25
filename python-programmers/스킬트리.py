def solution(skill, skill_trees):
    answer = 0
    skill_ele = list(skill)
    for skill_tree in skill_trees:
        order = []
        for s in skill_tree:
            if s in skill_ele:
                order.append(s)
        if order == skill_ele[: len(order)]:
            answer += 1
    return answer