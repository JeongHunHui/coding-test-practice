def make_dict():
    big_a_num = ord('A')
    big_z_num = ord('Z')
    new_dict = {}
    for i in range(big_a_num, big_z_num + 1):
        new_dict[chr(i)] = i - big_a_num + 1
    return new_dict

def solution(msg):
    msg_dict = make_dict()
    answer = []
    current_input = msg[0]
    for i in range(1, len(msg)):
        next_input = msg[i]
        word = current_input + next_input
        if word not in msg_dict:
            answer.append(msg_dict[current_input])
            msg_dict[word] = len(msg_dict) + 1
            current_input = next_input
        else:
            current_input = word
    answer.append(msg_dict[current_input])
    return answer