class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        s = list(s)
        for i in range(len(s)):
            if s==list(goal):
                return True
            else:
                left = s.pop(0)
                s.append(left)
        return False
                