class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack=[]
        for num in asteroids:
            while stack and stack[-1]>0 and num<0:
                if stack[-1]>abs(num):
                    break
                elif stack[-1]==abs(num):
                    stack.pop()
                    break
                else:
                    stack.pop()
            else:
                stack.append(num)
        return stack
       