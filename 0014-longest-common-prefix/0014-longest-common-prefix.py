class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        i = 0
        while i < len(strs[0]):
            ch  = strs[0][i]
            for j in range(1,len(strs)):
                if i >= len(strs[j]) or strs[j][i] != ch:
                    return prefix
            prefix += ch
            i += 1
        return prefix
       


        




        