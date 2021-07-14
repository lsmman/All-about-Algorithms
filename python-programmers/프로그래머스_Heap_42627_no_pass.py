# 통과 못함
def solution(jobs):
    def get_time_taken(jobs):
        answer = 0
        cur = 0
        done = [False for _ in range(len(jobs))]
        job = len(jobs)
        while job:
            for i, (srt, dur) in enumerate(jobs):
                if not done[i] and srt <= cur:
                    print(cur, cur + dur - srt, srt, dur)
                    done[i] = True
                    cur = dur + cur
                    answer += cur - srt
                    job -= 1
                    break
        return answer // len(jobs)

    jobs.sort(key=lambda x: x[0])
    fcfs = get_time_taken(jobs)
    jobs.sort(key=lambda x: x[1])
    sjf = get_time_taken(jobs)

    return min(fcfs, sjf)