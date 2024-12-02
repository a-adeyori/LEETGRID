class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        leftPointer=0
        rightPointer=len(s)-1

        while leftPointer<rightPointer:
            for i in range(len(s)//2):
                s[leftPointer],s[rightPointer]=s[rightPointer],s[leftPointer]
                leftPointer+=1
                rightPointer-=1


#more optimal according to Claude.AI
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        leftPointer=0
        rightPointer=len(s)-1

        while leftPointer<rightPointer:
            s[leftPointer],s[rightPointer]=s[rightPointer],s[leftPointer]
            leftPointer+=1
            rightPointer-=1