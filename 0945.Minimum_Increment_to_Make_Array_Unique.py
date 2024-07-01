class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = 0
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                newValue = nums[i - 1] + 1
                total += newValue - nums[i]
                nums[i] = newValue

        return total
