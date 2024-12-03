class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        # If all letters are capital
        if word.isupper():
            return True

        # If all letters are lowercase
        if word.islower():
            return True

        # If only first letter is capital
        if word[0].isupper() and word[1:].islower():
            return True

        return False

