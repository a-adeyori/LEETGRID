#usig two pointers
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = s.split(" ")
        words =[]
        for i in list_s:
            if i != "":
                words.append(i)

        left = 0
        right = len(words) -1

        print(words)

        while left < right:
            words[left],words[right] = words[right],words[left]
            left+=1
            right-=1

        return " ".join(words)
    
#using one line 0ms
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.strip().split()[::-1])