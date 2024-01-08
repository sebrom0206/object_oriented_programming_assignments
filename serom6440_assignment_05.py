# Assignment 5

# task 1

# all the binary trees (BT1, BT2 & BT3) are full binary trees
print(f'Task 1:\nall the binary trees (BT1, BT2 & BT3) are full binary trees\n')


# Task 2

def binary_tree(r):
    return [r, [], []]


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def insert_left_child(root, new_branch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right_child(root, new_branch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root

def make_tree():

    my_tree = binary_tree('1')

    insert_left_child(my_tree, '2')
    insert_right_child(my_tree, '3')

    insert_left_child(get_left_child(my_tree), '4')
    insert_left_child(get_right_child(my_tree), '5')
    insert_right_child(get_right_child(my_tree), '6')

    return my_tree


print(f'Task 2:\n{make_tree()}\n')


# Task 3


def build_my_graph2():
    class Graph:
        graph = dict()
        searched = []

        def add_edge(self, node, neighbour):
            if node not in self.graph:
                self.graph[node] = [neighbour]
            else:
                self.graph[node].append(neighbour)

        def print_graph(self):
            print(self.graph)

        def print_edges(self):

            for nodes in self.graph:
                for neighbour in self.graph[nodes]:
                    print("(", nodes, ", ", neighbour, ")")

        def depht_first_search(self, node):

            if node not in self.searched:
                print('[', node, end=' ], ')

                self.searched.append(node)
                if node in self.graph:
                    for neighbour in self.graph[node]:
                        self.depht_first_search(neighbour)

    my_graph = Graph()
    my_graph.add_edge('A', 'B')
    my_graph.add_edge('A', 'C')
    my_graph.add_edge('B', 'C')
    my_graph.add_edge('B', 'D')
    my_graph.add_edge('C', 'E')
    my_graph.add_edge('D', 'E')
    my_graph.add_edge('D', 'G')
    my_graph.add_edge('D', 'H')
    my_graph.add_edge('E', 'F')
    my_graph.add_edge('F', 'C')
    #my_graph.print_graph()

    my_graph.depht_first_search('A')


print('Task 3:')
build_my_graph2()
print('\n')


# Task 4

class BinarySearchTree:
    li_of_nodes = []

    def __init__(self, value=None):
        self.value = value
        if self.value:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None

    def is_empty(self):
        return self.value is None

    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()

            self.li_of_nodes.append(value)  # jalla

        elif value < self.value:
            self.left_child.insert(value)

        elif value > self.value:
            self.right_child.insert(value)

    def compute_sum(self):
        res = 0

        for i in self.li_of_nodes:
            res += i
        return res

    def compute_count(self):

        return len(self.li_of_nodes)


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)

print('Task 4:')
print('sum:', my_tree.compute_sum())
print('number of nodes:', my_tree.compute_count())
