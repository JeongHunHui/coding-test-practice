char_arr = ['A', 'E', 'I', 'O', 'U']
words = []
count = 0;
answer = 0;

def dfs(depth, word, answer_word):
    global count
    global answer
    if depth == len(char_arr):
        return
    for i in range(len(char_arr)):
        count += 1
        word += char_arr[i]
        if word == answer_word:
            answer = count
            break
        dfs(depth+1,word,answer_word)
        word = word[0:-1]
        
    

def solution(word):
    dfs(0, "", word)
    return answer
    