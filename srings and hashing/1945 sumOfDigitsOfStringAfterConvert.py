class Solution(object):
    def getLucky(self, s, k):
        val_str=''
        for num in s:
            val_str+=str(ord(num.lower()) - ord('a') +1)

        i=0
        while i<k:
            total=0
            total=sum(int(j) for j in val_str)
            val_str=str(total)
            i+=1

        return int(total)


       

        