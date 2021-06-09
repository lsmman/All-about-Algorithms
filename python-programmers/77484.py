# 로또의 최고 순위와 최저 순위
# 문제 유형 : 구현
# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/77484
# 문제 걸린 시간 : 5분

"""
문제 설명 : 
1부터 45 사이에 숫자를 맞추는 로또가 있습니다. 숫자가 일치한 수에 따라 아래 표와 같이 순위가 결정됩니다. 
로또를 구매한 민우는 당첨 번호 발표일을 학수고대하고 있었습니다. 하지만, 민우의 동생이 로또에 낙서를 하여, 일부 번호를 알아볼 수 없게 되었습니다. 당첨 번호 발표 후, 민우는 자신이 구매했던 로또로 당첨이 가능했던 최고 순위와 최저 순위를 알아보고 싶어 졌습니다.
알아볼 수 없는 번호를 0으로 표기하기로 하고, 민우가 구매한 로또 번호 6개가 44, 1, 0, 0, 31 25라고 가정해보겠습니다. 
당첨 번호 6개가 31, 10, 45, 1, 6, 19라면 당첨 가능한 최고 순위는 다음과 같습니다.
최고 순위는 31, 1번이 일치하고 0의 자리에 모두 당첨 번호가 들어가면 4개가 일치하므로 3등
최저 순위는 31, 1이 일치하여 2개가 일치하므로 5등

|순위 | 당첨 내용|
|1	|6개 번호가 모두 일치|
|2	|5개 번호가 일치|
|3	|4개 번호가 일치|
|4	|3개 번호가 일치|
|5	|2개 번호가 일치|
|6(낙첨) |그 외|
"""


def solution(lottos, win_nums):
    unknown = 0  # 지워져 값을 모르는 번호의 수
    win = 0  # 일치한 번호의 수
    rank = [6, 6, 5, 4, 3, 2, 1]  # index, value = 일치한 개수, 등수
    for l in lottos:
        if l == 0:  # 값이 지워진 경우
            unknown += 1
        elif l in win_nums:  # 번호가 당첨 번호 중 하나 일 때 = 일치할 때
            win += 1

    # 최선의 경우 : 밝혀진 값 중 일치한 번호와 값을 모르는 번호가 모두 당첨 번호일 때
    # 최악의 경우 : 모르는 번호는 모두 틀려서, 밝혀진 값 중 일치한 번호만 당첨 번호일 때
    return [rank[unknown + win], rank[win]]
