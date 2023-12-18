# 3 6 7 8 10 12 14 15 18 20
# N 개의 센서가 있다고 하면
# 오름차순 정렬 후 인접 센서간 거리를 구한다.
# | 3 | 1 | 1 | 2 | 2 | 2 | 1 | 3 | 2 |
# 그 뒤 센서간 거리를 내림차순으로 정렬해서 앞에서 부터 k-1개 제거
n = int(input())
k = int(input())
infos = sorted(list(map(int, input().split())))
dist = sorted([infos[i]-infos[i-1] for i in range(1, n)], reverse=True)
print(sum(dist[k-1:]))