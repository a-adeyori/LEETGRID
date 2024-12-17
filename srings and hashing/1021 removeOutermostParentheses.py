class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        balance = 0

        for i, char in enumerate(s):
            if char=='(':
                balance+=1
                if balance == 1:
                    start = i
            elif char == ')':
                balance-=1
                if balance ==0:
                    stack.append(s[start+1:i])
        return "".join(stack)
    

