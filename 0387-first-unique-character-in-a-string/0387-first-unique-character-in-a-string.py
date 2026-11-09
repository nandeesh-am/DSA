class Solution:
    def firstUniqChar(self, s: str) -> int:
        ht = {}
        for i in s:
            if i in ht :
                ht[i] += 1
            else:
                ht[i] = 1
        for i in range(len(s)):
            if s[i] in ht:
                if ht[s[i]] == 1:
                    return i
                    break
        return -1         
                  
        