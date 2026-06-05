#NODE OF A TREE
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


class BinaraySearchTree:
    #CREATES AN EMPTY FREE WITH NO NODES
    def __init__(self):
        self.root=None