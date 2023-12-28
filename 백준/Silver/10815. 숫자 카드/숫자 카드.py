# 17:48
n = int(input())
having_cards = set(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))
answer = []
for card in cards:
  if card in having_cards:
    answer.append('1')
  else:
    answer.append('0')
print(' '.join(answer))