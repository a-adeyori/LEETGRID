class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        #original train of thought
        # segment=s.split(' ')
        # filters=[]
        # for i in segment:
        #     if i != "":
        #         filters.append(i)
        # return len(filters)

        #realized optimized code
        segment=s.split()
        return len(segment)