import os, sys
import math
from abc import ABC, abstractmethod
from turtle import *

class Shape(ABC):
    """
    This is a abstract class representing geometrical shape.
    """

    def __init__(self, a=0, b=0, c=0, r=0):
        """
        Constructs Shape object

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        self.a = a
        self.b = b
        self.c = c
        self.r = r

        if any(isinstance(v, int) and v < 0 for v in vars(self).values()):
            raise ValueError('Values should be positive!')


    def get_area(self):
        """
        Calculates shape's area.

        Returns:
            float: area of the shape
        """
        if self.__class__.__name__ == 'circle':
            return math.pi * self.r ** 2

        elif self.__class__.__name__ == 'square' or self.__class__.__name__ == 'rectangle':
            return self.a * self.b

        elif self.__class__.__name__ == 'triangle' or self.__class__.__name__ == 'equilateral triangle' and self.a + self.b > self.c and self.b + self.c > self.a:
            s = (self.a+self.b+self.c)/2
            return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        
        elif self.__class__.__name__ == 'regular pentagon':
            return self.a**2*math.sqrt(5*(5+2*math.sqrt(5)))/4



    def get_perimeter(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        if self.__class__.__name__ == 'circle':
            return 2 * math.pi * self.r

        elif self.__class__.__name__ == 'square' or self.__class__.__name__ == 'rectangle':
            return 2 * self.a + 2 * self.b

        elif self.__class__.__name__ == 'triangle' or self.__class__.__name__ == 'equilateral triangle':
            return self.a + self.b + self.c
        
        elif self.__class__.__name__ == 'regular pentagon':
            return 5 * self.a


    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information bout shape
        """
        class_dictionary = vars(self)
        out = self.__class__.__name__
        for k,v in class_dictionary.items():
            if v > 0:
                out += ' : ' + str(k) + ' = ' + str(v)
        return out

    @classmethod
    def get_area_formula(cls):
        """
        Returns formula for the area of the shape as a string.

        Returns:
            str: area formula
        """
        dict_area = {'circle':"πr^2", 'square':'a**2', 'rectangle':'a*b',
        'triangle':'1/2*a*h',"equilateral triangle":'1/2*a*h',
        'regular pentagon':"(a ** 2 * 1/2 * (5(5+2 * 1/2 *(5))))/4"}
        for k,v in dict_area.items():
            if cls.__name__ == k:
                return v

    @classmethod
    def get_perimeter_formula(cls):
        """
        Returns formula for the perimeter of the shape as a string.

        Returns:
            str: perimeter formula
        """
        dict_perimieter = {'circle':"2πr", 'square':'2a+2b', 'rectangle':'2a+2b',
        'triangle':'3a',"equilateral triangle":'a+b+c',
        'regular pentagon':"5a"}
        for k,v in dict_perimieter.items():
            if cls.__name__ == k:
                return v

class Circle(Shape):
    def __init__(self, r):
        super().__init__(self, self, self, r)
        


class Triangle(Shape):
    pass


class EquilateralTriangle(Triangle):
    pass


class Rectangle(Shape):
    pass


class Square(Rectangle):
    pass


class RegularPentagon(Shape):
    pass


class ShapeList:
    pass


def main():
    square = Shape(5)
    print(square)
    print(square.get_area_formula())
main()