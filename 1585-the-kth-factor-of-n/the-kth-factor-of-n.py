class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        a=[]
        for i in range(1,n+1):
            if n%i==0 or i%n==0:
                a.append(i)
        if len(a)>=k:
            return a[k-1]
        return -1

        