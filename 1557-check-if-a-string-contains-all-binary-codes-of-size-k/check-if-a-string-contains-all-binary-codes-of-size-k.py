class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        seen = set()
        for i in range(0,len(s) - k + 1):
             substring=s[i:i+k]
             seen.add(substring)
        return len(seen)==2**k