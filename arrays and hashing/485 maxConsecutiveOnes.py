class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_count = 0  # To store the maximum consecutive 1s
        current_count = 0  # To count the current streak of 1s
    
        for num in nums:
            if num == 1:
                current_count += 1
            else:
                max_count = max(max_count, current_count)
                current_count = 0
        
        # Final check for the last streak of 1s
        max_count = max(max_count, current_count)
        
        return max_count