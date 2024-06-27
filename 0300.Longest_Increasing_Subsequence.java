class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        if(n <= 1) return n;

        int[][] dp = new int[n][n+1];

        for(int[] rows : dp) {
            Arrays.fill(rows, -1);
        }

         return lis(nums, 0, -1, dp);
    }

    private int lis(int[] nums, int currentInd, int prevInd, int[][] dp) {

        if(currentInd == nums.length) return 0;

        if(dp[currentInd][prevInd+1] != -1) return dp[currentInd][prevInd+1];

        int skip = lis(nums, currentInd + 1, prevInd, dp);
        int select = -1;
        if(prevInd == -1 || nums[currentInd] > nums[prevInd]) {
            select = 1 + lis(nums, currentInd+1, currentInd, dp);
        }

        dp[currentInd][prevInd+1] = Math.max(skip, select);

        return dp[currentInd][prevInd+1];
    }

}
