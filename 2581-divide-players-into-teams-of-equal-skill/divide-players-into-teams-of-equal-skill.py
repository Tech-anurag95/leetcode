class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        target=sum(skill)//(len(skill)//2)
        chemistry=0
        while left<right:
            if skill[left]+skill[right]!=target:
                return -1
            chemistry+=skill[left]*skill[right]
            left+=1
            right-=1
        return chemistry