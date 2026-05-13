# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0 # Height of None is 0
            
            left_height = dfs(node.left)
            if left_height == -1: return -1 # Left is already unbalanced
            
            right_height = dfs(node.right)
            if right_height == -1: return -1 # Right is already unbalanced
            
            # Current node balance check
            if abs(left_height - right_height) > 1:
                return -1
            
            # If balanced, return height to parent
            return 1 + max(left_height, right_height)
        
        # If the result isn't -1, the tree is balanced
        return dfs(root) != -1


        