class Solution:
    def gardenNoAdj(self,n:int,paths:list[list[int]])->list[int]:
        colored=[0]*(n+1)
        choices=[1,2,3,4]
        graph=[[] for i in range(n+1)]
        for x,y in paths:
            graph[x].append(y)
            graph[y].append(x)
        for i in range(1,n+1):
            used=set()
            for children in graph[i]:
                if colored[children]!=0:  #wo color adjacent me filled hai isliye wo color used hai 
                    used.add(colored[children])
            for choice in choices:   #available choices
                if choice not in used:   # choice=choices available - used 
                    colored[i]=choice
                    break
        return colored[1:]





        #AVAILABLE =CHOICES 
        #USED= ADJACENT KE COLORS
        #NEEDED=AVAILABLE - USED