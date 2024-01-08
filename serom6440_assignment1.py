# Assignment 1

"""
 Task 1

- Using the Big O notation for binary search to calculate worst case steps. O(log n)
a) Persian dictionary with 171476 words will in worst case take 18 steps
b) English dictionary with 1100373 words will in worst case take 21 steps
c) Chinese dictionary with 260000 words will in worst case take 18 steps

"""


# Task 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, ' ', end='')
            temp = temp.next


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')

my_linked_list = linkedList()
my_linked_list.head = node1
node1.next = node2
node2.next = node3

my_linked_list.print_list()
print('\n')

# Task 3

my_list = [1, 2, 3, 4, 5]


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print_stack(self):
        print(self.items)


def reverse_list(li):
    rev_list = []
    my_stack = Stack()
    for _ in li:
        my_stack.push(_)

    while not my_stack.is_empty():
        rev_list.append(my_stack.pop())
    print(rev_list)


reverse_list(my_list)

