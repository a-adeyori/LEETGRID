class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        
        # Iterate through each element in nums
        for i in range(len(nums)):
            if nums[i] != val:
                # If the element is not equal to val, we place it at the k
                nums[k] = nums[i]
                k += 1
        return k