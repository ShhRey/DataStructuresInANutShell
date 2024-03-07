# Class to represent each Node of the Tree
class TreeNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

# Class to represent Tree Data Structure
class BinaryTree:
    def __init__(self, root):
        self.root = TreeNode(root)


    # Function for Inserting Element in Left Node
    def insertLeft(self, current_node, item):
        if current_node.left is None:
            current_node.left = TreeNode(item)
        else:
            new_node = TreeNode(item)
            new_node.left = current_node.left
            current_node.left = new_node

    # Function for Inserting Element in Right Node
    def insertRight(self, current_node, item):
        if current_node.right is None:
            current_node.right = TreeNode(item)
        else:
            new_node = TreeNode(item)
            new_node.right = current_node.right
            current_node.right = new_node


    # Function for Searching Element in Tree
    def searchNode(self, root, item):
        if root is None:
            return False
        if root.item == item:
            return
        search_left = self.searchNode(root.left, item)
        search_right = self.searchNode(root.right, item)
        if search_left:
            return True
        if search_right:
            return True
        else:
            print(f"{item} Not Found in Tree !")


tree = BinaryTree(1)
tree.insertLeft(tree.root, 2)
tree.insertRight(tree.root, 3)
tree.insertLeft(tree.root.left, 4)
tree.insertRight(tree.root.right, 5)