# inorder, preorder, postorder - speaking of root
# time complexity recursive: O(n) n is # of vertex
# space complexity O(h) h is height of bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
#   return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
#   return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

# binary tree use cases: https://www.baeldung.com/cs/applications-of-binary-trees#:~:text=In%20computing%2C%20binary%20trees%20are,insertion%2C%20deletion%2C%20and%20traversal.
# bst use cases: sort, search, insert delete https://stackoverflow.com/questions/2130416/what-are-the-applications-of-binary-trees
