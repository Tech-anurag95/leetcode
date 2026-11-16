class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # s=total
        while len(s)>k:
            total=""
            for i in range(0,len(s),k):
                curr=0
                for num in s[i:i+k]:
                    curr+=int(num)
                total+=str(curr)
            s=total
        return s

        
