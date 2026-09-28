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