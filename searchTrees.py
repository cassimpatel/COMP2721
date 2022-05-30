class SearchTreeNode():
    key = None
    info = None

    left = None
    right = None
    parent = None

    # constructor, repr, copy, deepcopy
    # inorder, preorder, postorder
    # minimum, maximum, predecessor, successor
    pass

class BinarySearchTree():
    root = None

    # constructor, repr, copy, deepcopy
    # isEmpty
    # member, lookup, insert, delete
    # minimum, maximum
    # inorder, preorder, postorder
    pass

class RedBlackNode(SearchTreeNode):
    colour = None

    # constructor, repr, copy, deepcopy
    pass

class RedBlackTree():
    # constructor, repr, copy, deepcopy
    # insert, delete, leftRotation, rightRotation
    pass

class AVLNode(SearchTreeNode):
    pass

class AVLTree():
    pass

if __name__ == "__main__":
    print("Testing search trees")
    print()