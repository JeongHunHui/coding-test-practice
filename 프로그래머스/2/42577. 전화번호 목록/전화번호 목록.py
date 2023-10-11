def solution(phone_book):
    phone_dict = {}
    for phone in phone_book:
        phone_dict[phone] = 1
    for phone in phone_book:
        temp = ""
        for num in phone:
            temp += num
            if temp in phone_dict and temp != phone:
                return False
    return True