from collections import defaultdict

def solution(n, results):
    # winners: key = 선수 / data = key가 이긴 사람들의 집합
    # losers: key = 선수 / data = key가 진 사람들의 집합
    winners, losers = defaultdict(set), defaultdict(set)
    # 결과를 돌며 dict에 값 삽입
    for winner, loser in results:
        winners[winner].add(loser)
        losers[loser].add(winner)
    # 모든 선수들에 대해 승자와 패자 업데이트
    for i in range(1,n+1):
        # i가 j에게 패배 -> i에게 패배한 선수들(winners[i])은 j에게도 패배함
        for j in losers[i]:
            winners[j].update(winners[i])
        # i가 j에게 승리 -> i에게 승리한 선수들(losers[i])은 j에게도 승리함
        for j in winners[i]:
            losers[j].update(losers[i])
    # 자신이 승리한 사람과 패배한 사람의 수가 n-1이면 순위가 결정된 것
    return sum([1 for i in range(1,n+1) if len(winners[i])+len(losers[i]) == n-1])