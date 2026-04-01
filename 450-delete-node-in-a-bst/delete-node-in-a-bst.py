class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None
        if key<root.val:
            root.left=self.deleteNode(root.left, key)
        elif key>root.val:
            root.right=self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            min_node = self.findMin(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)

        return root

    def findMin(self, node):
        while node.left is not None:
            node=node.left
        return node