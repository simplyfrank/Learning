"""
Recursively defined collection of nodes that are related in an inheritance structure.



Coursera Algorithm Class   https://www.coursera.org/learn/data-structures/lecture/95qda/trees
"""


class Node(object):
    """
    Data Structure that has parent and child pointers
    """
    def __init__(self, id_):
        self.id = id_
        self.children = []
        self.parent = []
    
    def add_child(self, child):
        child.parent = self.id
        self.children.append(child)
        
    
    def get_children(self):
        return self.children

    def get_rev_children(self):
        children = self.children[:]
        children.reverse()
        return children




# ---------------

def create_tree(height=2, branching_factor=5):
    """
    Sets up a random Tree to be traversed with a certain height and a certain branching factor.
    """
    # nodes = [Node('{}{}'.format(n,i)) for n in range(branching_factor) for i in range(height) ]
    
    tree = Node('start')
    for i in range(branching_factor):
        subtree = Node('a{}'.format(i))
        for j in range(height):
            subtree.add_child(Node('a_sub{}'.format(j)))
        tree.add_child(subtree)
    return tree








