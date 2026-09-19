class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        arr.sort()
        median=arr[(len(arr)-1)//2]
        a=[]
        for i in range(len(arr)):
            strength=abs(median-arr[i])
            a.append((strength,arr[i]))
        a.sort(reverse=True)
        return [x[1] for x in a[:k]]