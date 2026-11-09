class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rht = {}
        mht = {}

        for i in ransomNote:
            rht[i] = rht.get(i, 0) + 1

        for i in magazine:
            mht[i] = mht.get(i, 0) + 1

        for i in rht:
            if i not in mht or rht[i] > mht[i]:
                return False

        return True

             