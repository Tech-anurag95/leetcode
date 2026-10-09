class Solution:
    def primePalindrome(self,n:int)->int:
        def prime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        if 8<=n<=11:
            return 11
        while True:
            s=str(n)
            if len(s)%2==0:
                n=10**len(s)
                continue
            if s==s[::-1]:
                if prime(n):
                    return n
            n+=1