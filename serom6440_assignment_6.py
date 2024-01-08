# Assignment 6

# Task 1

# a)

# Task 2

class QuizGift:

    def __init__(self):
        self.questions = [(120, 15), (200, 20), (150, 40), (350, 50), (100, 20), (90, 10)]
        self.gifts = ['watch', 'smartphone', 'laptop']

    def compute_result(self):
        max_points = [0] * 101
        for time_left in range(1, 101):
            for points, time in self.questions:
                if time <= time_left:
                    max_points[time_left] = max(max_points[time_left], max_points[time_left - time] + points)
        self.max_points = max_points

        if max_points[100] >= 750:
            self.gift = self.gifts[2]
        elif max_points[100] >= 250:
            self.gift = self.gifts[1]
        else:
            self.gift = self.gifts[0]

    def print_result(self):
        print(f"Maximum points: {self.max_points[100]}")
        print(f"Gift: {self.gift}")

quiz = QuizGift()
quiz.compute_result()
quiz.print_result()

# Task 3

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def compute_area(self):
        pass


class Square(Shape):
    def __init__(self, side_of_square):
        self.side_of_square = side_of_square

    def compute_area(self):
        print(f'Area of square: {self.side_of_square * self.side_of_square}')


class Circle(Shape):
    def __init__(self, radius_of_circle):
        self.radius_of_circle = radius_of_circle

    def compute_area(self):
        print(f'Area of circle: {math.pi * self.radius_of_circle ** 2:.2f}')


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def compute_area(self):
        s = (self.a + self.b + self.c) / 2
        triangle_area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print(f'Area of triangle: {triangle_area}')


square = Square(2)
square.compute_area()
print()
circle = Circle(2)
circle.compute_area()
print()
triangle = Triangle(5, 4, 3)
triangle.compute_area()
print()


# Task 4

class House:
    house_count = 0

    def __init__(self, owner, price, condition, cost=0, sold=False):
        self.owner = owner
        self.price = price
        self.condition = condition
        self.cost = cost
        self.sold = sold
        House.house_count += 1

    def sell(self, new_owner):
        self.owner = new_owner
        self.sold = True
        print(f'profit: {self.price - self.cost}')

    def change_price(self, new_price):
        if self.sold is True:
            print('House has been sold!')
        else:
            self.price = new_price

    def renovate(self, expense, new_condition):
        self.cost += expense
        self.condition = new_condition
        print('House renovated!')

    def print_info(self):

        print(f'{self.owner}, Condition: {self.condition}, Price: {self.price}$')

    def number_of_houses(self):
        print(f'Total number of houses:{self.house_count}')


house1 = House('John', 100000, 'Good')
house2 = House('Sara', 250000, 'Bad')

house1.print_info()
house2.print_info()

house1.renovate(50000, 'Great!')
house1.sell('Leo')

house1.print_info()
print(House.house_count)
