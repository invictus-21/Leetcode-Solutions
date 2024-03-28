from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # If the tree is empty, return an empty list
        if not root:
            return []

        # Initialize stack with the root node
        stack = [root]
        # Initialize result list
        res = []

        # Perform iterative postorder traversal
        while stack:
            # Pop the top node from the stack
            node = stack.pop()
            # Append the node's value to the result list
            res.append(node.val)
            # Add children of the node to the stack
            stack.extend(node.children)
        # Return the result list in the reverse order for correct postorder traversal
        return res[::-1]
