# 21:33
# -> k가 주어지면 이게 몇번째 피보나치 수인지 확인
# 0 1 2 3 4 5 6 7
# 0 1 1 2 3 5 8 13

# 32 -> 33,7
# 10xxxxx
# -> 1~피보5개까지 -> 12 가지
# -> 32-fibo[7]-fibo[6]
# -> 11 -> 12,5
# -> 10xxx
# -> 11-fibo[5]-fibo[4]
# -> 3 -> 4, 3
# -> 10x
# -> 4-fibo[3]-fibo[2]
# -> 1
# -> 0
# -> 1010100

k = int(input())
fibo = [0, 1]
i = 1
total = 1
while total < k:
  i += 1
  num = fibo[i-1] + fibo[i-2]
  total += num
  fibo.append(num)

answer = ''
while i > 0:
  new_k = k - fibo[i] - fibo[i-1]
  if new_k >= 0 and i >=2:
    answer += '10'
    k = new_k
    i -= 2
  elif new_k >= 0:
    answer += '1'
    i -= 1
  else:
    answer += '0'
    i -= 1
print(answer)