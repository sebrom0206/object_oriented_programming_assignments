# Assignment 3

# Task 1

#"""
print('''
Task 1: 
loops through each character in each string, word for word.
takes the ascii value of each individual character and adds them together + length of word/string
And then does modulo operation with chosen number (my_choice = 19)

Output is the values of the sum of ASCII values of individual characters+len(word)%19(my_choice)
output = 59166
'a1b2c3' = 5
'CiTiBnk' = 9
'232323' = 16
'myLaptop' = 6

When printing out the total var for each word it returns 480 for 'a1b2c3'
But I get 450 when doing it manually. Remainder 30 values?
Example
a 1 c 2 b 3 + len = 6
97 + 49 + 98 + 50 + 99 + 51  = 450

450 % 19 = 13 ?
480 % 19 = 5?
''')

#"""

"""
def hash_function(inp_str, table_size):
    tot = 0
    length = len(inp_str)
    print(length)

    for pos in range(length):
        tot += ord(inp_str[pos]) + length
        print(ord(inp_str[pos]))

    print(tot)

    return tot % table_size


my_list = ['a1b2c3', 'CiTiBnk', '232323', 'myLaptop']
my_choice = 19

for item in my_list:
    print(item)
    print(hash_function(item, my_choice), end=' ')
"""


# Task 2 HashClass
import hashlib as hl
import random


class HashClass:

    def __init__(self, id_num):
        self.id_num = self.hash_it(id_num)

    def hash_it(self, id_num):
        salt = random.randint(1, 1000)
        var = str(salt + id_num)
        self.id_num = hl.sha1(var.encode()).hexdigest()
        return self.id_num

    def print_it(self):
        print(self.id_num)


print('task 2, hashed int: ')
my_hash = HashClass(11011999)
my_hash.print_it()
print()

# Task 3 Sort and print
list_of_tuples = [('Birds of Prey', 97.1), ('Dolittle', 175.0), ('The Gentlemen', 7.0), ('Falling', 22.0)]


def sort_and_print(list_of_tups):
    n = 1

    for i in range(len(list_of_tups)):
        smallest_index = i

        for j in range(i + 1, len(list_of_tups)):

            if list_of_tups[smallest_index][n] < list_of_tups[j][n]:
                smallest_index = j
        list_of_tups[i], list_of_tups[smallest_index] = list_of_tups[smallest_index], list_of_tups[i]

    largest_budget = list_of_tups[0][0]

    print(f'The movie with the largest budget is: \n{largest_budget}')


print('Task 3, sort and print:')
sort_and_print(list_of_tuples)
print()

# Task 4 Most frequent integer
my_list = [10, 2, 5, 2, 0, 5, 6, 8, 5, 10]


def most_frequent_integer(li):
    my_dict = {}
    count = 0
    output = ''
    for i in reversed(li):
        my_dict[i] = my_dict.get(i, 0) + 1
        if my_dict[i] >= count:
            count, output = my_dict[i], i
    return output


print('Task 4, most frequent int:')
res = most_frequent_integer(my_list)
print(res)
print()


# Task 5 Recursive magic function


def magic_function(string):
    if len(string) == 1:
        return string

    permutations = magic_function(string[1:])
    # print(permutations)
    first_char = string[0]
    # print(first_char)
    res = []

    for i in permutations:
        for j in range(len(i) + 1):
            res.append(i[:j] + first_char + i[j:])

    return res


print('Task 5, permutations:')
print(magic_function('abcd'))

