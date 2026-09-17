class Solution:
    def compress(self, chars: list[str]) -> int:
        a=[]
        count=1
        n=len(chars)
        for i in range(n):
            if i+1<n and chars[i]==chars[i + 1]:
                count += 1
            else:
                a.append(chars[i])
                if count>1:
                    a.extend(str(count))
                count=1
        chars[:]=a
        return len(a)