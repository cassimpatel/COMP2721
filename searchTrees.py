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

    def copy(self):
        newObj = SearchTreeNode(self.key, self.info, self.parent)
        if self.left is not None:
            newObj.left = self.left.copy()
        if self.right is not None:
            newObj.right = self.right.copy()
        return newObj

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.key, " ", end="")
        if self.right is not None:
            self.right.inorder()
        
    def preorder(self):
        print(self.key, " ", end="")
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()

    def postorder(self):
        if self.left is not None:
            self.left.postorder()
        if self.right is not None:
            self.right.postorder()
        print(self.key, " ", end="")

    def minimum(self):
        r = self
        while r.left is not  None:
            r = r.left
        return r

    def maximum(self):
        r = self
        while r.right is not None:
            r = r.right
        return r

    def predecessor(self):
        n = self
        if n.left is not None:
            return n.left.maximum()
        else:
            p = n.parent
            while p is not None and n is p.left:
                n = p
                p = p.parent
            return p

    def successor(self):
        n = self
        if n.right is not None:
            return n.right.minimum()
        else:
            p = n.parent
            while p is not None and n is p.right:
                n = p
                p = p.parent
            return p

class BinarySearchTree():
    root = None

    def __init__(self, root=None):
        self.root = root

    def __repr__(self):
        return "Binary Search Tree with root ({})".format(self.root)

    def copy(self):
        newObj = BinarySearchTree()
        if self.root is not None:
            newObj.root = self.root.copy()
        return newObj

    def isEmpty(self):
        return self.root is None

    def inorder(self):
        print("Printing inorder traversal")
        self.root.inorder()
        print()

    def preorder(self):
        print("Printing preorder traversal")
        self.root.preorder()
        print()

    def postorder(self):
        print("Printing postorder traversal")
        self.root.postorder()
        print()

    def minimum(self):
        self.root.minimum()

    def maximum(self):
        self.root.maximimum()

    def member(self, key):
        return self.search(key) is not None

    def search(self, key):
        r = self.root
        while r is not None and r.key != key:
            if key < r.key:
                r = r.left
            else:
                r = r.right
        return r

    def lookUp(self, key):
        node = self.search(key)
        if node is None:
            return None
        return node.info

    def insert(self, key, info=None):
        newObj = self.copy()
        
        r = newObj.root
        r2 = None # originally r' from lectures
        p = r
        n = SearchTreeNode(key, info)
        while p is not None:
            r2 = p
            p = p.left if n.key < p.key else p.right
        n.parent = r2
        n.left = None
        n.right = None
        if r2 is None:
            newObj.root = n
        else:
            if n.key < r2.key:
                # print(n, "to left of", r2)
                r2.left = n
            else:
                # print(n, "to right of", r2)
                r2.right = n
        return newObj

    def insertMultiple(self, keys, infos=None):
        if infos == None:
            infos = [None for x in range(len(keys))]
        newObj = self.copy()
        for i in range(len(keys)):
            newObj = newObj.insert(keys[i], infos[i])
        return newObj

    def delete(self, key):
        newObj = self.copy()
        node = newObj.search(key)
        newObj.remove(node)
        return newObj

    def remove(self, node):
        q = node
        if q.left is None or q.right is None:
            r2 = q
        else:
            r2 = q.successor()
            q.key = r2.key
            q.info = r2.info
        p = r2.left if r2.left is not None else r2.right

        # print(" q is", q, id(q))
        # print("r2 is", r2, id(r2))
        # print(" p is", p, id(p))
        
        if p is not None:
            p.parent = r2.parent
        if r2.parent is None:
            self.root = p
        else:
            if r2 is r2.parent.left:
                r2.parent.left = p
            else:
                r2.parent.right = p
        return self

class RedBlackNode(SearchTreeNode):
    colour = None

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def copy(self):
        pass

class RedBlackTree():
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def copy(self):
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

    x = BinarySearchTree()
    x = x.insertMultiple([15, 5, 3, 12, 10, 6, 7, 13, 16, 20, 18, 23])
    x.inorder()
    x.preorder()
    #x.postorder()
    print()
    
    # deletion is not working
    y = x.delete(13)
    y.inorder()
    y.preorder()
    
    print()