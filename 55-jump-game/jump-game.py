#u can go farthest nums[i]+i from any index i so if nums[i]+i>farthest mtlb last number se bda number koi aa gya iska mtlb hum end tak phch jayenge wrna nhi agar 

'''We are not actually jumping from one index to another.
We are continuously asking:
What is the farthest position I can reach so far?'''
class Solution:
    def canJump(self,nums):
        reach=0
        for i in range(len(nums)):
            if i >reach:
                return False
            reach=max(reach,nums[i]+i)
        return True
            