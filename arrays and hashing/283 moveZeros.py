#My own solution bruteforce,using pointer, passed wrong due to O(n^2) runtime
class Solution(object):
    def moveZeroes(self, nums):
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==0:
                    nums[i],nums[j]=nums[j], nums[i]
        return nums
    


#AI using assignment and pointer, i guess. Optimized to O(n)  runtime
class Solution(object):
    def moveZeroes(self, nums):
        non_zero=0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[non_zero]=nums[i]
                non_zero+=1

        for j in range(non_zero,len(nums)):
            nums[j]=0
        
        return nums