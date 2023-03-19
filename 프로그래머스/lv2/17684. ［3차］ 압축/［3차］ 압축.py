from collections import deque
def solution(msg):
    answer = []
    word_dict = {}
    start_index = ord('A')
    end_index = ord('Z')+1
    for i in range(start_index, end_index):
        word_dict[chr(i)] = i - start_index + 1
    queue = deque(msg)
    word = ''
    num = 0
    end_index = 27
    while queue:
        new_char = queue.popleft()
        word += new_char
        if word in word_dict:
            num = word_dict[word]
        else:
            word_dict[word] = end_index
            end_index += 1
            word = ''
            answer.append(num)
            queue.appendleft(new_char)
    answer.append(num)
    return answer