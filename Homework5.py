from collections import deque
def main():
    arr = input_array()
    reversed_arr = reverse_using_queue(arr)
    print("Reversed array:", reversed_arr)
def input_array():
    arr = list(map(int, input("Enter a list of numbers: ").split()))
    return arr
def reverse_using_queue(arr):
    q = deque()
    for num in arr:
        q.append(num)
    reversed_arr = []
    while q:
        reversed_arr.insert(0, q.popleft())
    return reversed_arr
if __name__ == '__main__':
    main()
