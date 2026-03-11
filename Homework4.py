def input_array():
    n = int(input("Enter number of elements in array: "))
    arr = []
    for i in range(n):
        value = int(input("Enter a value: "))
        arr.append(value)
    return arr
def reverse_using_stack(arr):
    stack = []
    for element in arr:
        stack.append(element)
    for i in range(len(arr)):
        arr[i] = stack.pop()
    return arr
def main():
    arr = input_array()
    print("Original array:", arr)
    reversed_arr = reverse_using_stack(arr)
    print("Reversed array:", reversed_arr)
if __name__ == '__main__':
    main()