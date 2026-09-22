class Solution:
    def numberOfSubstrings(self,s:str)->int:
        left=0
        count=0
        for right in range(len(s)):
            while set(s[left:right+1])=={'a','b','c'}:
                count+=len(s)-right#Agar s[left:right+1] me a, b, c teeno present hain, to right side me jitne bhi characters add karenge, substring me a, b, c already rahenge.
                left+=1
        return count