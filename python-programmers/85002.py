# 복서 정렬하기

def solution(weights, head2head):
    """
    1. 승률이 높은 복서의 번호가 앞쪽
    2. 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
    3. 자기 몸무게가 무거운 복서의 번호가 앞쪽
    4. 작은 번호가 앞쪽
    
    아직 붙어본 적 없다면 0%
    """
    n = len(weights)
    info = []
    
    for player, results in enumerate(head2head):
        rate = 0 if not (n - results.count("N")) else results.count("W") / (n - results.count("N"))
        win_over_weight = sum([int(weights[player] < weights[enemy]) for enemy, fight_result in enumerate(results) if fight_result == "W"])
        info.append([-rate, -win_over_weight, -weights[player], player])
            
    return [i[3]+1 for i in sorted(info)]