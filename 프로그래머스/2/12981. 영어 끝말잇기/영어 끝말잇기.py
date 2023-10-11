def solution(n, words):
    word_dict = {""}
    pre_char = words[0][0]
    for i in range(len(words)):
        word = words[i]
        if word not in word_dict and pre_char == word[0]:
            word_dict.add(word)
            pre_char = word[-1]
        else:
            return [i%n+1, i//n+1]
    return [0,0]