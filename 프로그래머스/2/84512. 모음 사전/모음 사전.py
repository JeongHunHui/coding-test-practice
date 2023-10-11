char_arr = ['A', 'E', 'I', 'O', 'U']
words = []
count = 0;
answer = 0;
is_finish = False

def dfs(depth, word, answer_word):
    global count, answer, is_finish
    for i in range(len(char_arr)):
        if depth == len(char_arr) or is_finish:
            return
        count += 1
        word += char_arr[i]
        if word == answer_word:
            answer = count
            is_finish = True
            return
        dfs(depth+1,word,answer_word)
        word = word[0:-1]
        
    

def solution(word):
    dfs(0, "", word)
    return answer
    