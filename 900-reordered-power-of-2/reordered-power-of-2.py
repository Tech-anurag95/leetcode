class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import Counter
        dic=Counter(str(n))
        i=0
        while len(str(2**i))<=len(str(n)):
            if Counter(str(2**i))==dic:
                return True
            i+=1
        return False