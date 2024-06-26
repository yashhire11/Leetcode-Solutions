class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int min_diff = INT_MAX;
        int closest_sum = 0;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for(int p1 = 0; p1 < n-2; ++p1){
            int p2 = p1+1, p3 = n-1;
            while(p2 < p3){
                int sum = nums[p1] + nums[p2] + nums[p3];
                if(sum > target) p3--;
                else if(sum < target) p2++;
                else return sum;
                int diff = abs(sum - target);
                if(diff < min_diff){
                    min_diff = diff;
                    closest_sum = sum;
                }
            }
        }
        return closest_sum;
    }
};0016.
