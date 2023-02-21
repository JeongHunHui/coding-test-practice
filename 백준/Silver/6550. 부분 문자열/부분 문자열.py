def solution(str):
    word, full_word = str.split(" ")
    for c in full_word:
        if c == word[0]:
            word = word[1:]
        if len(word) == 0:
            break
    print('Yes' if len(word) == 0 else 'No')

while True :
  try :
    solution(input())
  except :
    break