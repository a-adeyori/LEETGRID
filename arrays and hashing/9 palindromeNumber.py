class Solution(object):
    def isPalindrome(self, x):
        #normal range (11ms)
        back=-1
        backwards_str=''

        for i in range(len(str(x))):
            backwards_str+=str(x)[back]
            back-=1
        
        return backwards_str==str(x)


        #step range size
        back_str=''
        for i in range(-1,-(len(str(x))+1),-1):
            back_str+=str(x)[i]
        return back_str==str(x)

        #short(4ms)
        return str(x) == str(x)[::-1]