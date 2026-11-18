class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        num1=Counter(s)
        num2=Counter(t)
        return num1==num2