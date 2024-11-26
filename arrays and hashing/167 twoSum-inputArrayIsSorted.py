class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = {}

        for i,n in enumerate(numbers,start=1):
            diff =  target - n
            if diff in store:
                return sorted([i, store[diff]])
            else:
                store[n]=i


