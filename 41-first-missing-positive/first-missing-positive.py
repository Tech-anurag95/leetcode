class Solution:
    def firstMissingPositive(self,nums):
        s=set(nums) #too remove the duplicates and checking same number many times
        i=1  #start of positive integer
        while i in s:
            i+=1
        return i