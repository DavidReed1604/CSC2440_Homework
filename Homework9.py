class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
def input_tree():
    values = list(map(int, input("Enter tree values (space-separated): ").split()))
    root = None
    for v in values:
        root = insert(root, v)
    return root
def sum_divisible_by_5(root):
    if root is None:
        return 0
    total = 0
    if root.value % 5 == 0:
        total += root.value
    total += sum_divisible_by_5(root.left)
    total += sum_divisible_by_5(root.right)
    return total
def print_tree(root):
    if root is not None:
        print_tree(root.left)
        print(root.value, end=" ")
        print_tree(root.right)
root = input_tree()
print("Tree values (Inorder):")
print_tree(root)
print("\nSum of nodes divisible by 5:", sum_divisible_by_5(root))