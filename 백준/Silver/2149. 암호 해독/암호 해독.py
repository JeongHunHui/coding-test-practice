def get_key_arr(key):
  arr = []
  for i in range(0, len(key)):
    arr.append(key[i]+str(i))
  arr.sort()
  return [int(s[1]) for s in arr]

def get_answer_by_pw_arr_and_key_arr(pw_arr, key_arr):
  new_arr = ['' for _ in pw_arr]
  for i in range(len(pw_arr)):
    new_arr[key_arr[i]] = pw_arr[i]
  answer = ''
  for i in range(len(new_arr[0])):
    for j in range(len(new_arr)):
      answer += new_arr[j][i]
  return answer

key = input()
pw = input()
key_arr = get_key_arr(key)
pw_arr = [pw[i:i+int(len(pw)/len(key))] for i in range(0,len(pw),int(len(pw)/len(key)))]
print(get_answer_by_pw_arr_and_key_arr(pw_arr, key_arr))