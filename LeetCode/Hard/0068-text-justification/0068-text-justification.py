class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        arr = []
        s = words[0]
        for word in words[1:]:
            if len(s) + len(word) + 1 <= maxWidth:
                s += ' ' + word
            else:
                s_arr = s.split()
                blank = len(s_arr) - 1
                blank_count = maxWidth - len(s) + blank
                if blank == 0:
                    arr.append(s+' '*blank_count)
                    s = word
                    continue
                blank_avg, blank_left = divmod(blank_count, blank)
                if blank_left == 0:
                    arr.append((' '*blank_avg).join(s_arr))
                else:
                    answer = ''
                    for i in range(blank_left):
                        answer += s_arr[i] + ' '*(blank_avg+1)
                    for i in range(blank_left, blank):
                        answer += s_arr[i] + ' '*blank_avg
                    arr.append(answer + s_arr[-1])
                s = word
        arr.append(s+' '*(maxWidth-len(s)))
        return arr