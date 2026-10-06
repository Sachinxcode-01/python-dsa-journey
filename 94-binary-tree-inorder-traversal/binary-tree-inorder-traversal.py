class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Traverse to the leftmost node, pushing all nodes onto the stack
            while current:
                stack.append(current)
                current = current.left
            
            # Current is None here. Pop the top node, record its value,
            # and shift focus to its right subtree.
            current = stack.pop()
            result.append(current.val)
            current = current.right
            
        return result