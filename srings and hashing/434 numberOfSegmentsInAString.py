class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        # segment=s.split(' ')
        # filters=[]
        # for i in segment:
        #     if i != "":
        #         filters.append(i)
        # return len(filters)
        segment=s.split()
        return len(segment)