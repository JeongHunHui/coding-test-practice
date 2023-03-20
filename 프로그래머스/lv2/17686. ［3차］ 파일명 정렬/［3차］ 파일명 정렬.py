def split_file(file, index):
    [num, tail] = [0, 0]
    for i in range(0, len(file)):
        c = file[i]
        if c.isnumeric():
            num = i
            break
    for i in range(num+1, len(file)):
        c = file[i]
        if not c.isnumeric():
            tail = i
            break
    if tail == 0:
        tail = len(file)
            
    return [file[0:num], int(file[num:tail]), index]

def solution(files):
    answer = []
    temp = [split_file(files[i], i) for i in range(len(files))]
    temp_dict = {}
    for arr in temp:
        [head, num, index] = arr
        head = head.upper()
        num = int(num)
        if head in temp_dict:
            temp_dict[head].append([num, index])
        else:
            temp_dict[head] = [[num, index]]
    arr = [[c] + [data for data in temp_dict[c]] for c in temp_dict]
    arr.sort(key = lambda x: x[0])
    for i in range(len(arr)):
        new_arr = arr[i][1:]
        new_arr.sort(key = lambda x: x[0])
        for i in new_arr:
            answer.append(i[1])
    return [files[i] for i in answer]