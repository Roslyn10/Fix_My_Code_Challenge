#!/usr/bin/python3
"""A moule that defines a Square class"""

class Square():
    """A class representing a square with width and height attributes"""
    
    width = 0
    height = 0

    
    def __init__(self, *args, **kwargs):
        """Initializes the square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Perimiter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns the width and height of the square"""
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
