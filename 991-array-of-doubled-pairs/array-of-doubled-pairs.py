class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        dic=Counter(arr)
        for num in sorted(arr,key=abs):
            if dic[num]==0:
                continue
            if dic[2*num]==0:
                return False
            dic[num]-=1
            dic[2*num]-=1
        return True
        