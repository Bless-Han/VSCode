# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, node: Optional[TreeNode]) -> str:
        if not node:
            return ""

        left = self.traverse(node.left)
        right = self.traverse(node.right)

        subtree = str(node.val) + "(" + left + ")" + "(" + right + ")"

        if subtree in self.subtrees:
            if self.subtrees[subtree] == 1:
                self.ret.append(node)
            self.subtrees[subtree] += 1
        else:
            self.subtrees[subtree] = 1

        return subtree

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # Time Complexity: O(N)
        # Space Complexity: O(N)

        self.subtrees = {}
        self.ret = []

        self.traverse(root)
        return self.ret
