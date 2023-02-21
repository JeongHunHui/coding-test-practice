char_count = ord("z") - ord("a") + 1
z_index = ord("z")

def transform_str(s, num):
  answer = ""
  for c in s:
    index = ord(c)+num
    answer += chr(index if index <= z_index else index - char_count)
  return answer


def solution(pw, s):
  for i in range(0, char_count):
    if s in transform_str(pw, i):
      return i
  return -1

pw = input()
count = int(input())
words = []
for i in range(0,count):
  words.append(input())
for word in words:
  new_num = solution(pw, word)
  if new_num != -1:
    print(transform_str(pw,new_num))
    break