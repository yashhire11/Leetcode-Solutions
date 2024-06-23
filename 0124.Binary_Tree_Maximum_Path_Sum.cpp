class Solution {
public:
    
    int maxSum;
    
    int solve(TreeNode* root) {
        if(root == NULL)
            return 0;
        
        int l = solve(root->left);
        int r = solve(root->right);
        
        int a = l + r + root->val; //(1)
        
        int b = max(l, r) + root->val; //(2)
        
        int c = root->val; //(3)
        
        maxSum = max({maxSum, a, b, c});
        
        
        //most important part
        return max(b, c);
        
    }
    
    int maxPathSum(TreeNode* root) {
        maxSum = INT_MIN;
        
        solve(root);
        
        return maxSum;
        
    }
};
