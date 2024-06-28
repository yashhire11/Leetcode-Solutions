class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def pathSum_a(root, sum):
            if root == None: return 0
            res = 0
            if root.val == sum: res += 1
            res += pathSum_a(root.left, sum-root.val);
            res += pathSum_a(root.right, sum-root.val);
            return res
            
        if root == None: return 0
        return self.pathSum(root.left, sum) + pathSum_a(root, sum) + self.pathSum(root.right, sum)
