class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        #brute force :)
        output= []

        for i,j in zip(word1,word2):
            output.append(i) 
            output.append(j)

        if len(word1)<len(word2):
            output.extend(word2[len(word1):])
        elif len(word1)>len(word2):
            output.extend(word1[len(word2):])

        return ''.join(output)#