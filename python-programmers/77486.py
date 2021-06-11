# 다단계 칫솔 판매
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/77486
# 문제 유형 : 구현, 그래프
# 문제 걸린 시간 : 25분

"""
문제 설명
민호는 다단계 조직을 이용하여 칫솔을 판매하고 있습니다. 판매원이 칫솔을 판매하면 그 이익이 피라미드 조직을 타고 조금씩 분배되는 형태의 판매망입니다. 어느정도 판매가 이루어진 후, 조직을 운영하던 민호는 조직 내 누가 얼마만큼의 이득을 가져갔는지가 궁금해졌습니다. 예를 들어, 민호가 운영하고 있는 다단계 칫솔 판매 조직이 아래 그림과 같다고 합시다.

민호는 center이며, 파란색 네모는 여덟 명의 판매원을 표시한 것입니다. 각각은 자신을 조직에 참여시킨 추천인에 연결되어 피라미드 식의 구조를 이루고 있습니다. 조직의 이익 분배 규칙은 간단합니다. 모든 판매원은 칫솔의 판매에 의하여 발생하는 이익에서 10% 를 계산하여 자신을 조직에 참여시킨 추천인에게 배분하고 나머지는 자신이 가집니다. 모든 판매원은 자신이 칫솔 판매에서 발생한 이익 뿐만 아니라, 자신이 조직에 추천하여 가입시킨 판매원에게서 발생하는 이익의 10% 까지 자신에 이익이 됩니다. 자신에게 발생하는 이익 또한 마찬가지의 규칙으로 자신의 추천인에게 분배됩니다. 단, 10% 를 계산할 때에는 원 단위에서 절사하며, 10%를 계산한 금액이 1 원 미만인 경우에는 이득을 분배하지 않고 자신이 모두 가집니다.
칫솔의 판매에서 발생하는 이익은 개당 100 원으로 정해져 있습니다.
예를 들어, 아래와 같은 판매 기록이 있다고 가정하겠습니다. 
판매원 young 에 의하여 1,200 원의 이익이 발생했습니다. young 은 이 중 10% 에 해당하는 120 원을, 자신을 조직에 참여시킨 추천인인 edward 에게 배분하고 자신은 나머지인 1,080 원을 가집니다. edward 는 young 에게서 받은 120 원 중 10% 인 12 원을 mary 에게 배분하고 자신은 나머지인 108 원을 가집니다. 12 원을 edward 로부터 받은 mary 는 10% 인 1 원을 센터에 (즉, 민호에게) 배분하고 자신은 나머지인 11 원을 가집니다. 
"""

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