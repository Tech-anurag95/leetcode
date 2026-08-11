class Solution:
    def largestOddNumber(self, num: str) -> str:
        diff=""
        for i in range(1,len(num)+1):
            if num[i-1] in "13579":
                diff=num[:i]
        return diff