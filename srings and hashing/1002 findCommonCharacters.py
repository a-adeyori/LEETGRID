from collections import Counter
class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output= []
        common_count = Counter(words[0])

        for word in words[1:]:
            common_count &= Counter(word)

        for letter, count in common_count.items():
            output.extend([letter]*count)
        return output
        