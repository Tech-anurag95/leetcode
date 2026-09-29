class Solution:
    def canArrange(self,arr: List[int],k: int)->bool:
        dic={}
        for num in arr:
            rem=num%k
            dic[rem]=dic.get(rem,0)+1

        for rem in dic:
            if rem==0:
                if dic[rem]%2!=0:
                    return False
            else:
                if dic.get(k-rem,0)!=dic[rem]:
                    return False

        return True