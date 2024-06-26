class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_overall = nums[0]
        max_ending_here, min_ending_here = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            tmp = max_ending_here
            max_ending_here = max({nums[i], nums[i]*max_ending_here, nums[i]*min_ending_here})
            min_ending_here = min({nums[i], nums[i]*tmp, nums[i]*min_ending_here})
            max_overall = max(max_overall, max_ending_here)
        
        return max_overall
