class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value, root=None):
        if root is None:
            root = self.root
        
        if root is None:
            self.root = Node(value)
        else:
            if value <= root.value:
                if root.left_child is None:
                    root.left_child = Node(value)
                else:
                    self.insert(value, root.left_child)
            else:
                if root.right_child is None:
                    root.right_child = Node(value)
                else:
                    self.insert(value, root.right_child)
        return None

    def preorder(self, node):
        if node != None:
            print(node.value, end=" ")
            self.preorder(node.left_child)
            self.preorder(node.right_child)
    def inorder(self, node):
        if node != None:
            self.inorder(node.left_child)
            print(node.value, end=" ")
            self.inorder(node.right_child)
    def postorder(self, node):
        if node != None:
            self.postorder(node.left_child)
            self.postorder(node.right_child)
            print(node.value, end=" ")
tree = Tree()

tree.insert(5)
tree.insert(-2)
tree.insert(7)
tree.insert(-1)
tree.insert(0)
tree.insert(6)

tree.preorder(tree.root)
print("")
tree.inorder(tree.root)
print("")
tree.postorder(tree.root)