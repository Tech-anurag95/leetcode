from collections import deque
class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n=len(parent) 
        tree=[[] for i in range(n)]  # hum array se tree bna rhe hain
        for i in range(1,n):
            tree[parent[i]].append(i)
        dic={}
        queue=deque([0])
        level=0
        while queue:
            size=len(queue)
            level+=1
            for i in range(size):
                node=queue.popleft()
                dic[node]=level
                for child in tree[node]:    #ye ek n ary tree hain(more than 2 nodes possible)
                    queue.append(child)
        ans=0
        height=level
        for m in range(n):
            ans+=nums[m]*(height-dic[m]+1)
        return ans