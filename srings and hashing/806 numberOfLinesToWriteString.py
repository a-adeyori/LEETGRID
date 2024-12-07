from collections import defaultdict
class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        store= defaultdict(int)
        sumLine=0
        lines=[]
        result= []

        for i in range(len(s)):
            store[s[i]]=widths[ord(s[i]) - ord('a')]

        print(store)
        for i in s:
            if sumLine<100 and not sumLine+store[i]>100:
                sumLine+=store[i]
            else:
                lines.append(sumLine)
                sumLine=0
                sumLine+=store[i]
        lines.append(sumLine)
        
        print(lines)

        result.append(len(lines))
        result.append(lines[-1])
        

        return result
    # print(numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"abcdefghijklmnopqrstuvwxyz"))
