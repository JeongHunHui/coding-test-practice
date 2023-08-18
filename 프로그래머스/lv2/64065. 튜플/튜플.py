def solution(s):
    num_list = []
    for nums in s[2:-2].split('},{'):
        num_list.append(list(map(int, nums.split(','))))
    num_list.sort(key = len)
    answer = []
    for nums in num_list:
        for num in nums:
            if num not in answer:
                answer.append(num)
                break
    return answer