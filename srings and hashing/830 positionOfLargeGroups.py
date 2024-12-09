class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        #to be review, practice with consecutive ones
        result = []
        n = len(s)
        i = 0

        while i < n:
            start = i
            # Move i until the character changes
            while i < n - 1 and s[i] == s[i + 1]:
                i += 1
            # End of the group
            end = i
            # Check if the group is large
            if end - start>= 2:
                result.append([start, end])
            i += 1  # Move to the next character

        return result