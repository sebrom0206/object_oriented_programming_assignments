# Assignment 2

"""
Task 1

original list:

[ 1001, 1030, 1050, 1020, 300, 1080, 1100]

after 3 passes of Selection sort (with smallest) the list will look like this:

[ 300, 1001, 1020, 1050, 1030, 1080, 1100]

Task 2

List of numbers to sort with bubble sort:

[210, 15, 111, 90, 45, 120, 150, 200, 100, 140 ]

partially sorted list after 3 swaps of bubble sort:

[15, 111, 90, 210, 45, 120, 150, 200, 100, 140 ]

partially sorted list after 3 passes of bubble sort:

[15, 45, 90, 111, 120, 150, 200, 100, 140, 210]

"""

# Task 3
my_list = [5, 4, 3, 2, 1, 2, 3, 4, 5]


def sort_and_rem_dup(li):
    no_dupes = []

    for i in range(len(li) - 1, 0, -1):

        for j in range(i):

            if li[j] > li[j + 1]:
                temp = li[j]
                li[j] = li[j + 1]
                li[j + 1] = temp

    for i in li:
        if i not in no_dupes:
            no_dupes.append(i)
    return no_dupes


new_list = sort_and_rem_dup(my_list)

print(f'Sorted list without duplicates: {new_list}')
print()


# Task 4

def check_palindrome(word):
    class Stack:
        def __init__(self):
            self.items = []

        def is_empty(self):
            return self.items == []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def print_stack(self):
            print(self.items)

    class Queue:
        def __init__(self):
            self.items = []

        def is_empty(self):
            return self.items == []

        def enqueue(self, item):
            self.items.insert(0, item)

        def dequeue(self):
            return self.items.pop()

        def size(self):
            return len(self.items)

        def print_queue(self):
            print(self.items)

    # word in stack

    word_stack = Stack()
    for char in word:
        word_stack.push(char)

    # word_stack.print_stack()

    # word in queue

    word_queue = Queue()
    for char in word:
        word_queue.enqueue(char)

    # word_queue.print_queue()

    if word_stack.items == word_queue.items:
        print(f'{word} is a Palindrome')
    else:
        print(f'{word} is not a Palindrome')

    """
    while not word_stack.is_empty() and word_queue.is_empty():

        if word_stack.pop() == word_queue.dequeue():
            print('Palindrome')
        else:
            print('Not Palindrome')
    """


check_palindrome('civic')
check_palindrome('hello')
