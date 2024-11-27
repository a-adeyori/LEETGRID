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

#using two pointers
        left_pointer=0
        right_pointer=len(numbers)-1

        while left_pointer<right_pointer:
            if numbers[left_pointer]+numbers[right_pointer] == target:
                return [left_pointer+1, right_pointer+1]
            elif numbers[left_pointer]+numbers[right_pointer] > target:
                right_pointer-=1
            else:
                left_pointer+=1
