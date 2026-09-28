#for 1338 we will use counter and we will remove those element whose sum of frequencies is >half of length of array and we will find minimum of such set like for example of we have to remove 1,2,3 for making length of array half and in the same array if we remove 5,6 to make the length half then we will use 5,6

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        from collections import Counter
        freq=Counter(arr)
        frequencies=sorted(freq.values(),reverse=True)
        removed=0
        count=0
        for f in frequencies:
            removed+=f
            count+=1
            if removed>=len(arr)/2:
                break
        return count