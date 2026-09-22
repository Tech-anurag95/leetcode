class Solution:
    def numOfSubarrays(self,arr:list[int],k:int,threshold:int)->int:
        count=0
        current=sum(arr[:k])
        left=0
        right=k
        if current>=k*threshold:
            count+=1
        while right<len(arr):
            current-=arr[left]
            current+=arr[right]
            left+=1
            right+=1
            if current>=k*threshold:
                count+=1
        return count