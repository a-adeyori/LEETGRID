class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        output=[]
        i=0
        while i<len(nums):
            start=nums[i]
            while i <len(nums)-1 and nums[i]+1==nums[i+1]:
                i+=1
            end=nums[i]
            
            if start==end:
                output.append(str(start))
            else:
                output.append(str(start)+"->"+str(end))
            i+=1
        return output
        