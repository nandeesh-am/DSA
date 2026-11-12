class Solution:
    def largestOddNumber(self, num: str) -> str:
        s = len(num)
        maxnum = ""
        if (int(num[s-1])) % 2 == 1:
            return num
        else:
             for i in range(s-1,-1,-1):
                if int(num[i]) % 2 == 1:
                    for j in range(i+1):
                        maxnum += num[j]
                    return maxnum
                    

                   
        return ""

   
            
        