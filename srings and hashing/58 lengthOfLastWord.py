class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if " " not in s:
            return len(s)

        words=s.split(' ')
        last_index=-1
        for i in range(len(words)-1, -1 , -1):
            if len(words[i])>0:
                return len(words[i])
            else:
                continue
