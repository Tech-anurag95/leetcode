class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        choice="abcdefghijklmnopqrstuvwxyz"
        s=list(s)
        gap=0
        for i in range(len(s)-1,-1,-1):
            gap=(gap+shifts[i])%26
            index=choice.index(s[i])
            s[i]=choice[(index+gap)%26]
        return ''.join(s)