class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        count=1
        for i in range(len(arr)-1):
            if max(arr[0:i+1]) <= min(arr[i+1:]):
                count+=1
        return count

        