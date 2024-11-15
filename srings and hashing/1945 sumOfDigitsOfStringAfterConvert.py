class Solution(object):
    def getLucky(self, s, k):
        val_str=''
        for num in s:
            val_str+=str(ord(num.lower()) - ord('a') +1)

        i=0
        while i<k:
            total=0

            for j in val_str:
                total+=int(j)
            convert=str(total)
            
            val_str = convert
            i+=1

        return int(total)
