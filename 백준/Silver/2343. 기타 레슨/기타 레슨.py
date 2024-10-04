# 00:57
# n개의 강의를 m개의 블루레이에 나눠 담기
# 단, 블루레이의 크기를 최소화, 블로레이는 용량 제한이 있음, 순서 유지해야함
# 가능한 최소 블루레이 크기를 찾자

# 블루레이 최소 크기는 각 강의 중 가장 긴 강의의 길이 이상
# 최대 크기는 모든 블루레이의 길이의 합
# 이진탐색?

n, m = map(int, input().split())
records = list(map(int, input().split()))

def binary_search():
    left = max(records)
    right = sum(records)

    while left <= right:
        mid = (left + right) // 2
        temp = 0
        count = 1 # 블루레이 수
        for record in records:
            # 현재 블루레이에 강의를 넣을 수 없다면?
            if temp + record > mid:
                count += 1
                temp = record
            else:
                temp += record
        # 블루레이 수가 m개 이하면 더 작게
        if count <= m:
            right = mid - 1
        # 너무 작으면 크게
        else:
            left = mid + 1
    # 가능한 최소 블루레이 크기
    return left

print(binary_search())