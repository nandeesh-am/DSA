class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        freq1 = {}
        if len(t) != len(s):
            return False
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        for char in t:
            if char in freq1:
                freq1[char] += 1
            else:
                freq1[char] = 1
        return freq == freq1
        
                 

        
             
        