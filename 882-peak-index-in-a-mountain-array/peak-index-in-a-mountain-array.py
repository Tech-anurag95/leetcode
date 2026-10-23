
#O(n) SOLUTION
'''class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return i'''

#O(logN) SOLUTION
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left=0
        right=len(arr)-1
        while left<right:
            mid=(left+right)//2
            if arr[mid]<arr[mid+1]:
                left=mid+1
            else:
                right=mid
        return left

'''if arr[mid]<arr[mid+1]: mtlb abhi bhi left element is smaller than right element mtlb peak abhi right side me hoga isliye humne left=mid+1 kiya
else:left element is greater than right element so peak left me hoga isliye right=mid'''