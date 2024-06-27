/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
/*
class Solution {
public:
    int countNodes(TreeNode* root) {
        if(!root)
            return 0;
        return 1+countNodes(root->left)+countNodes(root->right);
    }
};
*/
class Solution {
    
public:
    int countNodes(TreeNode* root) {
        if(!root)
            return 0;
        
        int left_levels = 1;
        TreeNode *l=root->left;
        while(l)
        {
            l=l->left;
            left_levels+=1;
        }
        int right_levels = 1;
        TreeNode *r = root->right;
        while(r)
        {
            r=r->right;
            right_levels+=1;
        }
        if(left_levels==right_levels)
            return pow(2,left_levels)-1;
        
        return 1+countNodes(root->left)+countNodes(root->right);
    }
};



static int fastio = []() {
    #define endl '\n'
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(0);
    return 0;
}();
