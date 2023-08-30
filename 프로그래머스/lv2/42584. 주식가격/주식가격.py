def solution(prices):
    price_len = len(prices)
    answer = []
    for i in range(price_len):
        current_price = prices[i]
        sec = 0
        for j in range(i+1, price_len):
            sec += 1
            if current_price > prices[j]:
                break
        answer.append(sec)
    return answer