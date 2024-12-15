class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #shorter logic
        reverseString = s[::-1]
        listReverseString = reverseString.split()
        reverseListReverseString = listReverseString[::-1]
        return " ".join(reverseListReverseString)

        #brute force
        def reverse(word):
            wordList = list(word)
            left=0
            right=len(wordList)-1
            while left<right:
                wordList[left],wordList[right]=wordList[right],wordList[left]
                left+=1
                right-=1
            return ''.join(wordList)

        wordList = s.split()
        reverseList = []

        for word in wordList:
            reverseList.append(reverse(word))

        return " ".join(reverseList)

    print(reverseWords("Let's take LeetCode contest"))


        