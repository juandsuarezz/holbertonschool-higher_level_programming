#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)
    
    @property
    def width(self):

        return self.__width

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):

        return self.__x

    @x.setter
    def x(self, value):

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):

        return self.__y

    @y.setter
    def y(self, value):

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    
    
    def area(self):

        return self.__width * self.__height

    def display(self):

        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(' ', end="")
            for j in range(self.__width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):

        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]

        else:
            if len(kwargs) > 0:
                keys = kwargs.keys()
                for i in keys:
                    if i == 'id':
                        self.id = kwargs['id']
                    if i == 'width':
                        self.width = kwargs['width']
                    if i == 'height':
                        self.height = kwargs['height']
                    if i == 'x':
                        self.x = kwargs['x']
                    if i == 'y':
                        self.y = kwargs['y']

    def to_dictionary(self):

        dictionary = {}
        dictionary['id'] = self.id
        dictionary['width'] = self.width
        dictionary['height'] = self.height
        dictionary['x'] = self.x
        dictionary['y'] = self.y

        return dictionary
