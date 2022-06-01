import copy

class SearchTreeNode():
    key = None
    info = None

    left = None
    right = None
    parent = None

    def __init__(self, key, info=None, parent=None):
        self.key = key
        self.info = info
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        return "Search node {}:{}".format(self.key, self.info)

    def __copy__(self):
        newObj = SearchTreeNode(self.key, self.info, self.parent)
        if self.left != None:
            newObj.left = copy.copy(self.left)
        if self.right != None:
            newObj.right = copy.copy(self.right)
        return newObj

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key)
        if self.right is not None:
            self.right.inorder()
        
    def preorder(self):
        print(self.key)
        if self.left is not None:
            self.left.inorder()
        if self.right is not None:
            self.right.inorder()

    def postorder(self):
        if self.left is not None:
            self.left.inorder()
        if self.right is not None:
            self.right.inorder()
        print(self.key)

    def minimum(self):
        r = self
        while r.left != None:
            r = r.left
        return r

    def maximum(self):
        r = self
        while r.right != None:
            r = r.right
        return r

    def predecessor(self):
        n = self
        if n.left != None:
            return n.left.maximum()
        else:
            p = n.parent
            while p != None and n == p.left:
                n = p
                p = p.parent
            return p

    def successor(self):
        n = self
        if n.right != None:
            return n.right.minimum()
        else:
            p = n.parent
            while p != None and n == p.right:
                n = p
                p = p.parent
            return p

    # lt, gt opreators?

class BinarySearchTree():
    root = None

    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return "Binary Search Tree with root ({})".format(self.root)

    def __copy__(self):
        newObj = BinarySearchTree()
        newObj.root = copy.copy(self.root)
        return newObj

    def isEmpty(self):
        return self.root == None

    def inorder(self):
        self.root.inorder()

    def preorder(self):
        self.root.preorder()

    def postorder(self):
        self.root.postorder()

    def minimum(self):
        self.root.minimum()

    def maximum(self):
        self.root.maximimum()

    def member(self):
        pass

    def lookUp(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass

class RedBlackNode(SearchTreeNode):
    colour = None

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __copy__(self):
        pass

class RedBlackTree():
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __copy__(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass

    def leftRotation(self):
        pass

    def rightRotation(self):
        pass

class AVLNode(SearchTreeNode):
    # init, repr, copy, height
    pass

class AVLTree():
    # init, repr, copy, insert, delete, leftRotation, rightRotation etc.
    pass

if __name__ == "__main__":
    print("Testing search trees")
    print()