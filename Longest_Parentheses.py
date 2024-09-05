def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [] 
        stack.append(-1)
        count = 0 
        for i in range(0, len(s)):
            if s[i] == "(": 
                stack.append(i)
            else: 
                stack.pop()
                if stack:
                    count = max(count, i-stack[-1])
                else: stack.append(i)
        return count 