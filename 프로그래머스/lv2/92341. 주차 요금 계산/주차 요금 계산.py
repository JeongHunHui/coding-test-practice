import math

def solution(fees, records):
    [base_time, base_fee, unit_time, unit_fee] = fees
    
    fee_dict = {}
    
    def get_minute(time_str):
        [hour, minute] = list(map(int, time_str.split(':')))
        return minute + hour * 60
    
    def get_term(start, end):
        return get_minute(end) - get_minute(start)
    
    def calculate_fee(time):
        total_time = time - base_time
        if total_time <= 0: return base_fee
        return math.ceil(total_time / unit_time) * unit_fee + base_fee
    
    for record in records:
        [time, num, in_out] = record.split(' ')
        if in_out == 'IN':
            fee_dict[num] = [0, time] if num not in fee_dict else [fee_dict[num][0], time]
        else:
            [total_time, start] = fee_dict[num]
            fee_dict[num] = [total_time + get_term(start, time), '']
            
    car_nums = list(fee_dict.keys())
    car_nums.sort()
    
    answer = []
    for car_num in car_nums:
        [total_time, time] = fee_dict[car_num]
        if time: total_time += get_term(time, '23:59')
        answer.append(calculate_fee(total_time))
    return answer

    
    