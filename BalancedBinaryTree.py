class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 1

class BalancedBinaryTree:
    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left_child = self.insert(root.left_child, value)
        else:
            root.right_child = self.insert(root.right_child, value)

        root.height = 1 + max(self.get_height(root.left_child), self.get_height(root.right_child))

        if self.get_balance_index(root) > 1:
            if value < root.left_child.value:
                return self.rotate_right(root)
            else:
                root.left_child = self.rotate_left(root.left_child)
                return self.rotate_right(root)

        if self.get_balance_index(root) < -1:
            if value > root.right_child.value:
                return self.rotate_left(root)
            else:
                root.right_child = self.rotate_right(root.right_child)
                return self.rotate_left(root)
        return root

    def rotate_left(self, node):
        aux_node = node.right_child
        ref = aux_node.left_child
        aux_node.left_child = node
        node.right_child = ref
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        aux_node.height = 1 + max(self.get_height(aux_node.left_child), self.get_height(aux_node.right_child))
        return aux_node

    def rotate_right(self, node):
        aux_node = node.left_child
        ref = aux_node.right_child
        aux_node.right_child = node
        node.left_child = ref
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        aux_node.height = 1 + max(self.get_height(aux_node.left_child), self.get_height(aux_node.right_child))
        return aux_node

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance_index(self, root):
        if not root:
            return 0
        return self.get_height(root.left_child) - self.get_height(root.right_child)

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

tree = BalancedBinaryTree()
root = None

amount = int(input())

for _ in range(amount):
    root = tree.insert(root, int(input()))

tree.preorder(root)
print("")
tree.inorder(root)
print("")
tree.postorder(root)
