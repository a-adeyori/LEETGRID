from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        total = 0
        store = Counter(chars)

        for word in words:
            storeWord = Counter(word)

            if all(storeWord[char] <= store[char] for char in storeWord):
                total+=len(word)
        
        return total

            