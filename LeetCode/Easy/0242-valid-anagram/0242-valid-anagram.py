class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash, tHash = Counter(s), Counter(t)
        sKeys, tKeys = set(sHash.keys()), set(tHash.keys())
        if sKeys != tKeys:
            return False
        for key in sKeys:
            if sHash[key] != tHash[key]:
                return False
        return True