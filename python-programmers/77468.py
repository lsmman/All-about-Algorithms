# 다단계 칫솔 판매
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/77486
# 문제 걸린 시간 : 25분


def solution(enroll, referral, seller, amount):
    profits = [0] * len(enroll)
    name2idx = {name: idx for idx, name in enumerate(enroll)}
    name2idx["-"] = -1
    referral = list(map(lambda x: name2idx[x], referral))

    for name, profit in zip(seller, amount):
        idx = name2idx[name]
        profit = profit * 100
        while idx != -1 and profit:
            referral_profit = int(profit * 0.1)
            profits[idx] = profits[idx] + (profit - referral_profit)
            profit = referral_profit
            idx = referral[idx]
    return profits