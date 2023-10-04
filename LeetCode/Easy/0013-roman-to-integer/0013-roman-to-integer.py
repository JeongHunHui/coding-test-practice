class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        answer = 0
        i = 0
        while i < len(s):
            c = s[i:i+2]
            if c in roman_dict:
                answer += roman_dict[c]
                i += 1
            else:
                answer += roman_dict[c[0]]
            i += 1
        return answer