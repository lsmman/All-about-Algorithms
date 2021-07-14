import heapq


def solution(jobs):
    heapQ = []
    turn = 0
    time_taken = 0
    # 작업이 요청되는 시점을 기준으로 내림차순으로 job 정렬
    sorted_jobs = sorted(jobs, key=lambda x: x[0], reverse=True)

    while sorted_jobs or heapQ:
        # 정렬된 jobs 중 현재 turn 전에 요청된 job을 pop한 후
        # heapQ에 period가 짧은 순으로 정렬되도록 넣어준다.
        while sorted_jobs and turn >= sorted_jobs[-1][0]:
            start, period = sorted_jobs.pop()
            heapq.heappush(heapQ, [period, start])
        # 현재 turn전에 요청된 job이 들어간 heapQ에 job이 있다면 가장 period가 짧은 job을 pop한다.
        # 현재 turn을 꺼낸 job이 끝난 turn 시점으로 옮겨주고 걸린 시간을 더해준다.
        if heapQ:
            period, start = heapq.heappop(heapQ)
            turn = turn + period
            time_taken += turn - start
        # 현재 turn에 아직 들어온 job이 없다면 turn을 하나 늘려준다.
        else:
            turn += 1
    # 평균 걸린 시간 리턴 (총 걸린 시간 / job의 개수)
    return time_taken // len(jobs)


import unittest


class test(unittest.TestCase):
    def test_case(self):
        self.assertEqual(solution([[0, 3], [1, 9], [2, 6]]), 9)


unittest.main()