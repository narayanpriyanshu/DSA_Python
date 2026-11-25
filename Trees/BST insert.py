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

    def insert(self,value):
        new_node=Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp=self.root
        while temp:
            if temp.value < new_node.value:
                if temp.right is None:
                    temp.right=new_node
                    return True
                temp=temp.right
            elif temp.value > new_node.value:
                if temp.left is None:
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                return False     #ACCOUNTS FOR THE CASE WHEN SAME VALUE IS PRESENT IN THE LIST

my_tree=BinaraySearchTree()
my_tree.insert(5)
print(my_tree.root.value)