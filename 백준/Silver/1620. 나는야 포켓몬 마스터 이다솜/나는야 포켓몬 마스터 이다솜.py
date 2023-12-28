# 22:48
n, m = map(int, input().split())
pokemon_dict = {}
for num in range(1,n+1):
  name = input()
  pokemon_dict[str(num)] = name
  pokemon_dict[name] = str(num)
quiz_list = [input() for _ in range(m)]
for quiz in quiz_list:
  print(pokemon_dict[quiz])