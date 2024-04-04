# Question 1: Find the distance between two nodes ?
'''
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def path_to_ancestor(x, p):
    length = 0
    current_node = x
    while current_node != p:
        current_node = current_node.parent
        length += 1
    return length

def common_ancestor(node, u, v):
    if u.key < node.key and v.key < node.key:
        return common_ancestor(node.left, u, v)
    elif u.key > node.key and v.key > node.key:
        return common_ancestor(node.right, u, v)
    else:
        return node
    
def path_length(root, u, v):
    common_ancestor_node = common_ancestor(root, u, v)
    path_u_to_ancestor = path_to_ancestor(u, common_ancestor_node)
    path_v_to_ancestor = path_to_ancestor(v, common_ancestor_node)
    return path_u_to_ancestor + path_v_to_ancestor

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.parent = root
root.right.parent = root
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.left.left.parent = root.left
root.left.right.parent = root.left
u = root.left.left
v = root.left.right
distance = path_length(root, u, v)
print(distance)
'''

# Question 2: Mirror Binary Tree
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def mirror(root):
    if root is None:
        return
    
    root.left, root.right = root.right, root.left
    mirror(root.left)
    mirror(root.right)


def traverse(root):
    if root:
        traverse(root.left)
        print(root.value, end=" ")
        traverse(root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(traverse(root))
mirror(root)
print(traverse(root))
'''

# Question 3: Validate a Binary Tree
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def valid_BST(root, minval=float('-inf'), maxval=float('inf')):
    if root is None:
        return True
    
    if (root.value <= minval) or (root.value >= maxval):
        return False
    
    return(valid_BST(root.left, minval, root.value) and
           valid_BST(root.right, root.value, maxval))

root_valid = TreeNode(5)
root_valid.left = TreeNode(3)
root_valid.right = TreeNode(7)
root_valid.left.left = TreeNode(2)
root_valid.left.right = TreeNode(4)
root_valid.right.left = TreeNode(6)
root_valid.right.right = TreeNode(8)
print(valid_BST(root_valid))
'''