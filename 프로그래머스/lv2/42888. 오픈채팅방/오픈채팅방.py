def solution(record):
    chat_datas = []
    name_dict = {}
    for log in record:
        log_data = log.split(' ')
        [action, uid] = log_data[0:2]
        if action == "Change": name_dict[uid] = log_data[2]
        else:
            is_enter = action == "Enter"
            chat_datas.append([uid, is_enter])
            if is_enter: name_dict[uid] = log_data[2]
    return [f'{name_dict[chat_data[0]]}님이 {"들어왔" if chat_data[1] else "나갔"}습니다.' for chat_data in chat_datas]
