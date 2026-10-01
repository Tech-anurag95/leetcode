from collections import Counter
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def check(n):
            freq=Counter(str(n))
            for key,value in freq.items():
                if int(key)!=value:
                    return False
            return True
        n += 1
        while True:
            if check(n):
                return n
            n+=1