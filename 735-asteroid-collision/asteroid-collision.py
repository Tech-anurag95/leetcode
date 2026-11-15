class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack=[]
        for num in asteroids:
            while stack and num<0 and stack[-1]>0:
                if stack[-1]<abs(num):
                    stack.pop()
                elif stack[-1]==abs(num):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(num)
        return stack