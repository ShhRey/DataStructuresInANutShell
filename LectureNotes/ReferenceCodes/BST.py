class Node:
    def __init__(self, key):
        self.key = key
        self.leftchild = None
        self.rightchild = None
        self.parent = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if self.root is None:
            self.root = new_node
            return

        w = self.root
        p = None
        while w is not None:
            p = w
            if key < w.key:
                w = w.leftchild
            else:
                w = w.rightchild

        if key < p.key:
            p.leftchild = new_node
        else:
            p.rightchild = new_node
        new_node.parent = p

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.leftchild, key)
        return self._search_recursive(node.rightchild, key)

    def delete(self, k):
        w = self._search_recursive(self.root,k)  # Find the node w with key k
        if w is None:
            print("not found")
            return  # Node with key k not found

        if self._is_external(w):  # w has no children
            self._delete_external(w)
        elif w.leftchild is None or w.rightchild is None:  # w has just one child
            self._delete_one_child(w)
        else:  # w has two children
            self._delete_two_children(w)

    def _delete_external(self, w):
        if w.parent.leftchild == w:
            w.parent.leftchild = None
        else:
            w.parent.rightchild = None

    def _delete_one_child(self, w):
        if w.leftchild is None:  # w has just right child
            if w.parent.leftchild == w:  # w is its parent’s left child
                w.parent.leftchild = w.rightchild
            else:
                w.parent.rightchild = w.rightchild
            w.rightchild.parent=w.parent
        else:  # w has just left child
            if w.parent.leftchild == w:  # w is its parent’s left child
                w.parent.leftchild = w.leftchild
            else:
                w.parent.rightchild = w.leftchild
            w.leftchild.parent=w.parent

    def _delete_two_children(self, w):
        v = w.leftchild
        while v.rightchild is not None:
            v = v.rightchild
    #    if True: #v.parent!=w:

        p = v.parent
        c = v.leftchild
        v.parent = w.parent

        
        if w.leftchild != v:
            v.leftchild = w.leftchild

        v.rightchild = w.rightchild

        if p.rightchild == v:
            p.rightchild = c
        else:
            p.leftchild = c
        if c is not None:
            c.parent = p
        if w==self.root:
            self.root=v
        else:  
            if w.parent.rightchild == w:
                w.parent.rightchild = v
            else:
                w.parent.leftchild = v

            

    def _is_external(self, node):
        return node.leftchild is None and node.rightchild is None


    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.leftchild)
            print(node.key, end=" ")
            self._inorder_recursive(node.rightchild)


# Example usage:

bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
bst.insert(10)
bst.insert(25)


# Print the tree in inorder traversal
print("Inorder Traversal:", end=" ")
bst.inorder_traversal()  # Output: 2 3 4 5 6 7 8
print("\nAfter deleting")
bst.delete(50)
bst.inorder_traversal()  
