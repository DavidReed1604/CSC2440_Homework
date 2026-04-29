def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)
def heap_sort_decreasing(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        min_heapify(arr, i, 0)
def input_array():
    n = int(input("Enter number of elements: "))
    arr = []
    for i in range(n):
        value = int(input(f"Element {i + 1}: "))
        arr.append(value)
    return arr
def print_array(arr):
    print("Sorted array in decreasing order:")
    for value in arr:
        print(value, end=" ")
    print()
arr = input_array()
print("Original array:", arr)
heap_sort_decreasing(arr)
print_array(arr)