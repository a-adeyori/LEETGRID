class Solution(object):
    def plusOne(self, digits):
        string=''
        for  i in digits:
            string+=str(i)
        integer=int(string)
        plus_1= integer+1
        new_str= str(plus_1)
        new_list=[int(x) for x in new_str]
        return new_list