"""
How to efficiently traverse a tree.

- Dephth First Traversal
- Breadth First Traversal


Based on: Coursera Algorithms Class ::  https://www.coursera.org/learn/data-structures/lecture/fr51b/tree-traversal
"""
from queue import Queue
from tree import create_tree


def breadthFirst(root, return_values=False):
    """
    Traverses a tree by recursevly following the first available tree for each node we encounter.
    Once a Leaf is met, we recursively follow all next possible branches on the same tree, again following them down till we hit a node.

    This process continues till all nodes have been visited, or a goal match is satisfied.
    """
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        nodes.append(cur_node)
        for child in cur_node.get_children():
            stack.append(child)
    return [node.id for node in nodes] if return_values else nodes


def depthFirst(root, return_values=False):
    """
    Traverses a tree by recursively storing all possible children for a given node in a 'frontier queue' (FIFO) and then popping the first element.
    On this next node, the process is repeated. Once we hit a leaf node we break.

    In this fashion the process traverses the tree in order of height, visiting each sibling nodes before continuing to its further descendents.
    """
    nodes = []
    stack = [root]
    while stack:
        cur_node = stack[0]
        stack = stack[1:]
        nodes.append(cur_node)
        for child in cur_node.get_rev_children():
            stack.insert(0, child)
    return [node.id for node in nodes] if return_values else nodes






# ---------------------------- Example Traversals -----------------------------------------

# Create a sample Tree of given height and branching factor
tree = create_tree(height=2, branching_factor=5)

print(breadthFirst(tree, return_values=True))
print(depthFirst(tree, return_values=True))



