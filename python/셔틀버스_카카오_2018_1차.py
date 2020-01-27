def solution(n, t, m, timetable):
    answer = ''
    # 09:00 크루까지 탈 수 있음
    class shuttle():
        def __init__(self, hour, minute, rided = 0):
            self.hour = hour
            self.minute = minute
            self.rided = rided # num of rided person
        def __str__(self):
            print_hour = str(self.hour)
            print_minute = str(self.minute)
            if self.hour < 10:
                print_hour = ''.join(["0", print_hour])
            if self.minute < 10:
                print_minute = ''.join(["0"+ print_minute])
            return ':'.join([print_hour, print_minute])
        def minute_sub(self, subtract):
            if not self.minute:
                self.hour -= 1
                self.minute = 59
            else:
                self.minute = self.minute -1
            return self
        def get_time_value(self):
            return self.hour * 60 + self.minute
    
    hour = 9
    minute = 0
    shuttles = []
    idx_last_time_man_could_board = -1
    timetable = sorted(timetable)
    for _ in range(n):
        shuttles.append(shuttle(hour, minute))
        minute = minute + t
        if minute >= 60:
            hour = hour + (minute//60)
            minute = minute % 60
    timetable_search_idx = 0
    timetable_length = len(timetable)
    time_convert_value = 60
    for bus in shuttles:
        for idx in range(timetable_search_idx, timetable_length):
            if bus.rided == m:
                timetable_search_idx = idx
                idx_last_time_man_could_board = idx-1
                break
            crew_bus = list(map(int, timetable[idx].split(':')))
            crew_time_value = crew_bus[0] * time_convert_value + crew_bus[1]
            if crew_time_value <= bus.get_time_value():
                bus.rided += 1
            else :
                timetable_search_idx = idx
                break
            print(bus, bus.rided, timetable[idx])
    for bus in shuttles:
        print(bus, bus.rided)
    if shuttles[-1].rided < m:
        answer = str(shuttles[-1])
    else :
        fight_time = list(map(int, timetable[idx_last_time_man_could_board].split(':')))
        answer = str(shuttle(fight_time[0], fight_time[1]).minute_sub(1))
    return answer