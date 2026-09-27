class Solution:
    def lenLongestFibSubseq(self, arr):
        s=set(arr)
        ans=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                a=arr[i]
                b=arr[j]
                count=2
                while a+b in s:
                    a,b=b,a+b
                    count+=1
                ans=max(ans,count)
        return ans if ans>=3 else 0