import math

out = 'OUT'

def get_time(start, finish):
    start_hour, start_min = map(int, start.split(':'))
    finish_hour, finish_min = map(int, finish.split(':'))
    return 60 * (finish_hour - start_hour) + finish_min - start_min

def calculate_fee(fee_info, time):
    basic_time, basic_fee, time_term, term_fee = fee_info
    left_time = time - basic_time
    if left_time > 0:
        return basic_fee + math.ceil(left_time / time_term) * term_fee
    return basic_fee

def make_car_info_dict(records):
    car_dict = {}
    for record in records:
        time, num, in_out = record.split()
        if in_out == out:
            start_time, time_sum = car_dict[num]
            time_sum += get_time(start_time, time)
            car_dict[num] = [None, time_sum]
        elif num in car_dict:
            car_dict[num][0] = time
        else:
            car_dict[num] = [time, 0]
    
    for num in car_dict.keys():
        start_time, time_sum = car_dict[num]
        if start_time != None:
            time_sum += get_time(start_time, '23:59')
            car_dict[num] = [None, time_sum]
    
    return car_dict

def make_fee_list_by_car_dict(car_dict, fee_info):
    car_nums = sorted(car_dict.keys())
    return [calculate_fee(fee_info, car_dict[num][1]) for num in car_nums]

def solution(fees, records):
    car_dict = make_car_info_dict(records)
    return make_fee_list_by_car_dict(car_dict, fees)