class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root
def build_tree():
    root = None
    n = int(input("Enter number of nodes: "))
    print("Enter values:")
    for _ in range(n):
        val = int(input())
        root = insert(root, val)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
def sum_k_largest(root, k):
    stack = []
    current = root
    count = 0
    total_sum = 0
    while stack or current:
        while current:
            stack.append(current)
            current = current.right
        current = stack.pop()
        count += 1
        total_sum += current.data
        if count == k:
            kth_largest = current.data
            break
        current = current.left
    return sum_greater_equal(root, kth_largest)
def sum_greater_equal(root, k_value):
    if root is None:
        return 0
    if root.data >= k_value:
        return (root.data +
                sum_greater_equal(root.left, k_value) +
                sum_greater_equal(root.right, k_value))
    else:
        return sum_greater_equal(root.right, k_value)
root = build_tree()
print("Inorder traversal (sorted):")
inorder(root)

k = 3
result = sum_k_largest(root, k)
print("\nSum of elements >= kth largest:", result)