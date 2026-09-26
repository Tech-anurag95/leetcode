class Solution:
    def passwordStrength(self, password: str) -> int:
        count=0
        password=set(password)
        for char in password:
            if char.islower():
                count+=1
            elif char.isupper():
                count+=2
            elif char.isdigit():
                count+=3
            elif char in "!@#$":
                count+=5
        return count
        