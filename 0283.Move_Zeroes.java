class Solution {

    public void moveZeroes(int[] nums) {
        for(int i = 0, j = 0; j < nums.length; j++){
            if(nums[j] != 0){
                swap(nums, i++, j);
            }
        }
    }
    
    public void swap(int[] arr, int i, int j) {
        arr[i] = (arr[i] + arr[j]) - (arr[j] = arr[i]);
    }
}
