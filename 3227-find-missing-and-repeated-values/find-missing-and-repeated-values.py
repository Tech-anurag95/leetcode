# class Solution:
#     def findMissingAndRepeatedValues(self,grid:List[List[int]])->List[int]:
#         a={}
#         ans=[]
#         total=0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 a[grid[i][j]]=a.get(grid[i][j],0)+1
#                 total+=grid[i][j]
#         repeated=0
#         for key,value in a.items():
#             if value==2:
#                 repeated=key
#                 ans.append(key)
#         n=len(grid)
#         expected=sum(range(1,n*n+1))
#         missing=expected-(total-repeated)
#         ans.append(missing)

#         return ans

class Solution:
    def findMissingAndRepeatedValues(self,grid:List[List[int]])->List[int]:
        a={}
        ans=[]
        total=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                a[grid[i][j]]=a.get(grid[i][j],0)+1
                total+=grid[i][j]

        for key,value in a.items():
            if value==2:
                ans.append(key)
                total-=key

        array=[]
        for num in range(1,len(grid)*len(grid)+1):
            array.append(num)

        ans.append(sum(array)-total)
        return ans