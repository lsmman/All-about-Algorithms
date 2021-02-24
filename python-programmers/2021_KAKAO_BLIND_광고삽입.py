def time2sec(given_time):
    return sum(x * int(t) for x, t in zip([3600, 60, 1], given_time.split(":")))


def sec2time(sec):
    h, m, s = sec // 3600, sec % 3600 // 60, sec % 60
    return "{:02d}:{:02d}:{:02}".format(h, m, s)


def solution(play_time, adv_time, logs):
    cum_played = [0 for _ in range(360001)]
    play_sec = time2sec(play_time)
    adv_sec = time2sec(adv_time)
    max_adv_played = max_adv_sec = 0
    
    for log in logs:
        srt, end = log.split("-")
        cum_played[time2sec(srt)+1] += 1
        cum_played[time2sec(end)+1] -= 1
    for idx in range(1, play_sec + 1):
        cum_played[idx] += cum_played[idx - 1]
    for idx in range(1, play_sec + 1):
        cum_played[idx] += cum_played[idx - 1]

    for srt in range(play_sec-adv_sec+1):
        end = srt + adv_sec
        adv_played = cum_played[end] - cum_played[srt]
        if max_adv_played < adv_played:
            max_adv_played = adv_played
            max_adv_sec = srt

    return sec2time(max_adv_sec)

