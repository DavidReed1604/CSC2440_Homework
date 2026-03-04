class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
    def input_list(self):
        print("Input a list: ")
        for _ in range(7):
            value = int(input())
            self.insert(value)
    def prints(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        mid = self.get_middle(head)
        next_to_middle = mid.next
        mid.next = None
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)
        sorted_list = self.sorted_merge(left, right)
        return sorted_list
    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def sorted_merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        return result
    def average_even(self):
        temp = self.head
        total = 0
        count = 0
        while temp:
            if temp.data % 2 == 0:
                total += temp.data
                count += 1
            temp = temp.next
        if count == 0:
            return 0
        return total / count
def main():
    ll = LinkedList()
    ll.input_list()
    print("Original list: ")
    ll.prints()
    ll.head = ll.merge_sort(ll.head)
    print("Sorted list: ")
    ll.prints()
    avg = ll.average_even()
    print("Average of even numbers: ", avg)
if __name__ == '__main__':
    main()
