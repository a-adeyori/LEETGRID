class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        left = 0
        right = len(s)-1
        list_s = list(s)

        while left<right:
            if list_s[left].isalpha() and list_s[right].isalpha():
                list_s[left],list_s[right] = list_s[right],list_s[left]
                left+=1
                right-=1
            elif list_s[left].isalpha() and not list_s[right].isalpha():
                right-=1
            else:
                left+=1
        return "".join(list_s)
              