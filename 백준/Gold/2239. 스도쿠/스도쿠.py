# 22:50
# 좌측 상단 3*3에서 가장 낮은 수 부터 넣어보기
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
squares = [set() for _ in range(9)]
nums = []
for i in range(9):
  input_nums = list(map(int, [c for c in input()]))
  nums.append(input_nums)
  rows[i] = set(input_nums)
  for j in range(9):
    cols[j].add(input_nums[j])
    squares[i//3 * 3 + j//3].add(input_nums[j])

def new_pos(x, y):
  x += 1
  if x == 9:
    return (0, y+1)
  return (x, y)

answer = None
def backtracking(x, y):
  global answer
  if answer != None:
    return
  if y == 9:
    answer = '\n'.join([''.join(list(map(str, num))) for num in nums])
    return
  nx, ny = new_pos(x, y)
  if nums[y][x] != 0:
    backtracking(nx, ny)
    return
  for i in range(1, 10):
    if i not in rows[y] and i not in cols[x] and i not in squares[y//3 * 3 + x//3]:
      rows[y].add(i)
      cols[x].add(i)
      squares[y//3 * 3 + x//3].add(i)
      nums[y][x] = i
      backtracking(nx, ny)
      rows[y].remove(i)
      cols[x].remove(i)
      squares[y//3 * 3 + x//3].remove(i)
      nums[y][x] = 0

backtracking(0, 0)
print(answer)