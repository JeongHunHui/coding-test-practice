def solution(record):
    nickname_dict = {}
    def get_message(uid, act):
        nickname = nickname_dict[uid]
        return f'{nickname}님이 {"들어왔" if act == "Enter" else "나갔"}습니다.'
    
    info_list = []
    for log in record:
        info = log.split()
        act, uid = info[:2]
        if act != 'Leave':
            nickname = info[2]
            nickname_dict[uid] = nickname
        if act != 'Change':
            info_list.append([uid, act])
    answer = []
    for info in info_list:
        uid, act = info
        answer.append(get_message(uid, act))
    return answer
