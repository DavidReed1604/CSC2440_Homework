class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def insertPreorder(root,value):
    if root is None:
        return Node(value)
    if root.left is None:
        root.left = Node(value)
        return root
    else:
        inserted = insertPreorder(root.left, value)
        if inserted:
            return root
        if root.right is None:
            root.right = Node(value)
            return root
        else:
            inserted = insertPreorder(root.right, value)
            if inserted:
                return root
        return root
def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val, end=" ")
root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)
insertPreorder(root, 6)
print("Postorder traversal:")
postOrder(root)