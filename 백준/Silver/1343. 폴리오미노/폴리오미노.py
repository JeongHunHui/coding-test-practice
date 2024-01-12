def compress_blocks(s):
    answer = ''
    while s:
        if s[0] == '.':
            answer += '.'
            s = s[1:]
        else:
            a_count = s.find('.') if s.find('.') != -1 else len(s)
            if a_count % 2:
                return '-1'
            answer += 'AAAA' * (a_count // 4) + 'BB' * ((a_count % 4) // 2)
            s = s[a_count:]
    return answer

result = compress_blocks(input())
print(result)