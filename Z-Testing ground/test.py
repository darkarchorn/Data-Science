def rev(s):
        if s == "[":
            return "]"
        if s == "(":
            return ")"
        if s == "{":
            return "}"
        return ""

class Solution:
        
    def isValid(self, s: str) -> bool:
        op = ["[", "(", "{"]
        stack = []
        for i in s:
            if stack and stack[-1] in op and rev(stack[-1]) == i:
                stack.pop()
            else:
                stack.append(i)
        return stack == []
    
s = Solution()
print(s.isValid(s ='''([{}])'''))