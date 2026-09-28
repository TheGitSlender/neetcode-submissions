# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def is_identical(self, root, subroot):
        if root is None and subroot is None:
            return True
        if root is None or subroot is None:
            return False
        return (root.val == subroot.val and self.is_identical(root.right, subroot.right) and self.is_identical(root.left, subroot.left))


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes = [root]
        seen_nodes = []

        while nodes:
            current_node = nodes.pop()
            if self.is_identical(current_node, subRoot) == True:
                return True
            if current_node.right:
                nodes.append(current_node.right)
            if current_node.left:
                nodes.append(current_node.left)
        return False



            
                    