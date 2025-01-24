# 11:17
def is_valid(a, b, c):
  max_len = max([a,b,c])
  return max_len < (a+b+c)/2

def get_name(a, b, c):
  if a == b == c:
    return "Equilateral"
  if not is_valid(a, b, c):
    return "Invalid"
  if len(set([a, b, c])) == 3:
    return "Scalene"
  return "Isosceles"

lens = []

while True:
  a, b, c = map(int, input().split())
  if a == b == c == 0:
    break
  lens.append([a,b,c])

for a, b, c in lens:
  print(get_name(a,b,c))