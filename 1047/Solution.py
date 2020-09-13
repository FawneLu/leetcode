class Solution:
    def removeDuplicates(self, S: str) -> str:
        if not S or len(S) == 1:
            return S
        
        stack = []
        stack.append(S[0])
        
        for i in range(1, len(S)):
            if stack and S[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(S[i])
        return "".join(stack)