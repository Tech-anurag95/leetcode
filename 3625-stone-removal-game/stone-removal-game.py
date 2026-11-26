class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        x=10
        count=0
        while n>=x and x>0:
            count+=1
            n-=x
            x-=1
        if count%2==1:
            return True
        return False