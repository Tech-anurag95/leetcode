class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        kam=1
        jyada=max(piles)
        while kam<=jyada:
            total=0
            mid=(kam+jyada)//2
            for num in piles:
                total+=math.ceil(num/mid)
            if total<=h:  #jldi kha liya isliye speed kam krni hai 
                jyada=mid-1
            else:   #dheere khaya isliye speed bdhani hai 
                kam=mid+1
        return kam
        