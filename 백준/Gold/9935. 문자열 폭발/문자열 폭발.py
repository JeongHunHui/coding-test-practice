# 23:55
s, target = input(), [c for c in input()]
word, l = [], len(target)
for c in s:
  word.append(c)
  if word[-l:] == target:
    for _ in range(l):
      word.pop()
print(''.join(word) if word else 'FRULA')