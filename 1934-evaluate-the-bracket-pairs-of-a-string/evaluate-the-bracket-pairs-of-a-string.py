class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        for word in knowledge:
            if "(" + word[0] + ")" in s:
                s = s.replace("(" + word[0] + ")", word[1])
        while "(" in s:
            start = s.index("(")
            end = s.index(")", start)
            s = s[:start] + "?" + s[end + 1:]
        return s