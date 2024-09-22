def solution(n, t, m, timetable):
    # 9시 부터 n회 t분 간격
    # 한 셔틀에는 최대 m명
    # 셔틀을 타고 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각
    # 같은 시각에 도착한 크루 중 대기열에서 제일 뒤
    
    times = sorted([int(time.split(':')[0]) * 60 + int(time.split(':')[1]) for time in timetable])
    current_n = 0 # 현재 셔틀 운행 횟수
    current_m = 0 # 현재 셔틀 탑승 인원
    next_time = 540 # 다음 셔틀 시간
    last_time = 0 # 마지막 탑승 시간
    last_crew = 0 # 마지막 탑승객 index
    
    # 마지막 탑승객 1분 전에 타야됨
    while current_n < n:
        current_m = 0
        while True:
            if last_crew >= len(times):
                break
            time = times[last_crew]
            print(time, next_time, current_m, m)
            if time > next_time or current_m >= m:
                break
            current_m += 1
            last_crew += 1
            last_time = time
        next_time += t
        current_n += 1
    
    if last_time == 0:
        last_time = 540 + (n-1)*t
    elif current_m == m:
        last_time -= 1
    else:
        last_time = next_time - t
    print(last_time//60)
    print(last_time%60)
    hour_str = str(last_time//60)
    min_str = str(last_time%60)
    hour_str = f'0{hour_str}' if len(hour_str) == 1 else hour_str
    min_str = f'0{min_str}' if len(min_str) == 1 else min_str
    return f'{hour_str}:{min_str}'