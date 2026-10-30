class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        count=1
        for i in range(len(arr)-1):
            if max(arr[:i+1])==i:
                count+=1
        return count

#the elements start from 0 so the ith index must have i as the element
#so arr[:i+1] must have i as its max element 

        