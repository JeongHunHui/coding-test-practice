def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s.sort(key = lambda x: len(x))
    s = [list(map(int, data.split(','))) for data in s]
    
    for nums in s:
        for num in nums:
            if num not in answer:
                answer.append(num)
                break

    return answer