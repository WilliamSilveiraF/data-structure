priority = {
    0: "-",
    1: "+",
    2: "*",
    3: "/"
}

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class Tree:
    def  __init__(self):
        self.root = None

    def insert(self, value, node=None):
        if node == None:
            node = Node()
        
        if self.root == None:
            self.root = node
        
        if len(value) == 1:
            node.value = value
            return None
        
        for idx in range(0, 4):
            special_exp = priority[idx]
            if special_exp in value:
                special_exp_position = value.rfind(special_exp)
                node.value = value[special_exp_position]

                node.right_child = Node()
                node.left_child = Node()

                right_rest = value[special_exp_position+1:]
                left_rest = value[:special_exp_position]

                self.insert(right_rest, node.right_child)
                self.insert(left_rest, node.left_child)
                return

    def preorder(self, node):
        if node is not None:
            print(node.value, end="")
            self.preorder(node.left_child)
            self.preorder(node.right_child)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left_child)
            self.postorder(node.right_child)
            print(node.value, end="")

input_ = input()

tree = Tree()

tree.insert(input_)

tree.preorder(tree.root)
print("")
tree.postorder(tree.root)