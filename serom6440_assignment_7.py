# Assignment 7

# Exercise 1

# T(n) = O(n^3)

# Exercise 2
"""
n4 + n3 + 9 n2 + n log n + 5 <= (1+1+9+1+5)n^4 <= c.n^4
so c = 17 for n >= n0 = 1

constant is 17
"""


# Exercise 3

def my_func1(inputs):  # T(1)
    n = len(inputs)  # T(1)
    result = 0  # T(1)
    for i in range(n):  # iterates T(n) times
        j = 1  # T(1)
        while j < n:  # iterates T(log n), because j*2 each iteration
            result += inputs[i] * inputs[j]  # T(log n ), T(n)*T(log n)
            j *= 2
    return result  # T(1)


# O(my_func1) = 5 O(1) + O(n) + O(log n) + O(n)*O(log n)
# O(my_func1) = O(n log n)


def my_func2(inputs):  # T(1)
    n = len(inputs)  # T(1)
    for i in range(n - 1):
        for j in range(n - i - 1):  # T(n^2)
            if inputs[j] > inputs[j + 1]:  # T(1)
                tmp = inputs[j]  # T(1)
                inputs[j] = inputs[j + 1]  # T(1)
                inputs[j + 1] = tmp  # T(1)


# O(my_func2) = 6 O(1) + O(n^2)
# O(my_func2) = O(n^2)

# Exercise 4

def solve_problem(S):
    n = len(S)  # T(1)
    A = [0] * n  # T(1)
    total_sum = 0  # T(1)

    for i in range(n):
        total_sum += S[i]  # T(n)
        A[i] = total_sum / (i + 1)

    return A  # T(1)


"""
Takes a list of daily website usage and returns a list of average usage, A
Big O of solve_problem:
O(solve_problem) = O(n)
"""
