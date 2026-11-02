class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        size=len(palindrome)
        if size==1:
            return ""
        palindrome=list(palindrome)
        for i in range(size//2):
            if palindrome[i]!="a":
                palindrome[i]="a"
                return "".join(palindrome)
        palindrome[-1]="b"
        return "".join(palindrome)