class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        count = 0
        for i in range(len(s)-1):
            if s[i] == "(" :
                if count > 0:
                    ans += s[i] 
                count += 1
            
            else:
                count -= 1
                if count > 0:
                    ans += s[i] 
                
        return ans




        