class Solution:
    def numberOfSubarrays(self,nums:list[int],k:int)->int:
        a=[1]*len(nums)
        for i in range(len(nums)):
            if nums[i]%2==0:
                a[i]=0
        left=0
        ans=0
        total=0
        zeros=0
        for right in range(len(a)):
            total+=a[right]
            while total>k:  
                total-=a[left]   #agar sum bda aa gya to hum starting ke element ko nikal denge
                left+=1 #left ko ek aage 
                zeros=0
            if total==k:          #total humara target ke barabar aagya 
                while left<right and a[left]==0:  #agar left me 0 hain to unko nikalne se humare total me farak nhi pdega 
                    zeros+=1   #count of zeroes in left of the number till where the sum is target 
                    left+=1    #left ko ek aage bdhate jaa rhe hain
                ans+=zeros+1     #agar teen 0 hain to teeno nikal ke jo nyi subarray bnegi uska bhi sum same hi hoga isliye zero+1(ye 1 subse main aur original subarray ke liye hai)
        return ans
        