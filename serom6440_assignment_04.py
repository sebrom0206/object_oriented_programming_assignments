# Assignment 4

# Task 1

# Given the following Graph, which set represents the Edge set of the Graph?
# b) { (A,B), (B,C), (B,D), (C,A), (D,A) }
print('Task 1: \n\nb) { (A,B), (B,C), (B,D), (C,A), (D,A) }')
print()
# Task 2

COLUMNS = 'abcde'
NUM_QUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3
all_solutions = []


def solve(partial_sol):
    exam = examine(partial_sol)

    if exam == ACCEPT:
        # print(partial_sol) removing print(partial_sol), don't want it in the output
        all_solutions.append(partial_sol)  # adds valid solutions to "all_solution list"

    elif exam != ABANDON:
        for p in extend(partial_sol):
            solve(p)


# Examine function checks whether two queens in a partial solution can attack each other or not
def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):

            if attacks(partial_sol[i], partial_sol[j]):
                return ABANDON

    if len(partial_sol) == NUM_QUEENS:
        return ACCEPT
    else:
        return CONTINUE


# attacks function determines when two queens can actually attack each other
def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])

    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])

    return row1 == row2 or column1 == column2 or abs(row1 - row2) == abs(column1 - column2)


# Extend function takes a partial solution and makes different copies of it
# Each copy gets a new queen in a different column.
def extend(partial_sol):
    results = []
    row = len(partial_sol) + 1

    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))

        results.append(new_solution)

    return results


def is_solution(candidate_solution):
    sorted_cs = selection_sort(candidate_solution)

    for i in all_solutions:
        selection_sort(i)

    if sorted_cs in all_solutions:
        return 'Valid'
    else:
        return 'Invalid'


# Selection sort helper function, to sort all solutions and candidate_solution in order to check if valid or invalid
def selection_sort(li):
    n = 0  # nth is the column position
    for i in range(len(li)):
        smallest_index = i

        for j in range(i + 1, len(li)):

            if ord(li[smallest_index][n]) > ord(li[j][n]):  # using ord to sort with unicode values
                smallest_index = j

        li[i], li[smallest_index] = li[smallest_index], li[i]

    return li


print('Task 2: ')

solve([])
# print(all_solutions)
print()
candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']
result1 = is_solution(candidate_solution1)
result2 = is_solution(candidate_solution2)
print("Candidate Solution 1:", result1)
print("Candidate Solution 2:", result2)
print()


# Task 3

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

    def breadth_first_search(self, node):

        searched_bfs = [node]
        search_queue = [node]

        while search_queue:
            node = search_queue.pop(0)

            print('[', node, end=' ], ')

        if node in self.graph:
            for neighbour in self.graph[node]:
                if neighbour not in searched_bfs:
                    searched_bfs.append(neighbour)
                    search_queue.append(neighbour)

    def depht_first_search(self, node):

        if node not in self.searched:
            print('[', node, end=' ], ')

            self.searched.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depht_first_search(neighbour)

    def find_cycle(self, node):
        visited_nodes = {node: None}
        queue = [node]

        while queue:
            current_node = queue.pop(0)

            for neighbour in self.graph.get(current_node, []):
                if neighbour not in visited_nodes:
                    visited_nodes[neighbour] = current_node
                    queue.append(neighbour)
                elif visited_nodes[current_node] != neighbour:
                    return 'Cycle found'

        return 'cycle not found'


my_graph_task3 = Graph()
my_graph_task3.add_edge('A', 'B')
my_graph_task3.add_edge('B', 'D')
my_graph_task3.add_edge('C', 'B')
my_graph_task3.add_edge('C', 'J')
my_graph_task3.add_edge('D', 'E')
my_graph_task3.add_edge('D', 'F')
my_graph_task3.add_edge('E', 'C')
my_graph_task3.add_edge('E', 'G')
my_graph_task3.add_edge('F', 'H')
my_graph_task3.add_edge('G', 'I')

print('Task 3:\n')
result = my_graph_task3.find_cycle('A')
print(result)
print()


# Task 4

class Graph_T4:
    graph = dict()

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

    def remove_edges(self, node):
        del self.graph[node]


graph = Graph_T4()
graph.add_edge('a', 'b')
graph.add_edge('a', 'c')
graph.add_edge('b', 'c')
graph.add_edge('b', 'd')
graph.add_edge('c', 'd')
graph.add_edge('d', 'e')
print('Task 4: ')
print('\noriginal graph:')
graph.print_graph()
print()
graph.print_edges()
print()
graph.remove_edges('a')
print('after removal: ')
graph.print_graph()
print()
graph.print_edges()
