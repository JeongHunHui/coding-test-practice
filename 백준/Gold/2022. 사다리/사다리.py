# 22:51
x, y, c = [float(c) for c in input().split()]

def calculate(x, y, c):
    left, right = 0, min(x, y)
    num = 10 ** (-5) # 오차 범위
    while right - left > num:
        mid = (left + right) / 2  # 중간값
        h1 = (x**2 - mid**2)**0.5
        h2 = (y**2 - mid**2)**0.5
        if (h1 * h2) / (h1 + h2) > c:
            left = mid
        else:
            right = mid
    return left

print(f"{calculate(x, y, c):.3f}")