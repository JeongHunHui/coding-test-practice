import math

def get_time(start, finish):
    start_hour, start_min = map(int, start.split(':'))
    finish_hour, finish_min = map(int, finish.split(':'))
    return 60 * (finish_hour - start_hour) + finish_min - start_min

def solution(fees, records):
    basic_time, basic_fee, time_term, term_fee = fees
    def calculate_fee(time):
        left_time = time - basic_time
        return basic_fee + math.ceil(left_time / time_term) * term_fee if left_time > 0 else basic_fee
    car_dict = {}
    for record in records:
        time, num, in_out = record.split()
        is_in = in_out == 'IN'
        if is_in:
            if num in car_dict:
                car_dict[num][0] = time
            else:
                car_dict[num] = [time, 0]
        else:
            start_time, time_sum = car_dict[num]
            car_dict[num] = [None, time_sum + get_time(start_time, time)]
    car_nums = sorted(car_dict.keys())
    for num in car_nums:
        start_time, time_sum = car_dict[num]
        if start_time != None:
            time_sum += get_time(start_time, '23:59')
            car_dict[num] = [None, time_sum]
    return [calculate_fee(car_dict[i][1]) for i in car_nums]

    
    