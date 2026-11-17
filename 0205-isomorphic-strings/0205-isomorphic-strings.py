class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sh = {}
        th = {}
        for i in range(len(s)):
            if s[i] in sh:
                if sh[s[i]] != t[i]:
                    return False
            else:
                sh[s[i]] = t[i]
            if t[i] in th:
                if th[t[i]] != s[i]:
                    return False
            else:
                th[t[i]] = s[i]
        return True

            
        
        