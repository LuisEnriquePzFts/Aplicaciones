#bridge.py
class DrawingAPIOne(object):
    '''Implementation-specific abstraction:concrete class one'''
    def draw_circle(self, x, y, radius):
        print("API 1 drawing a circle at ({}, {} with radius {})".format(x, y, radius))
class DrawingAPITwo(object):
    '''Implementation-specific abstraction:concrete class one'''
    def draw_circle(self, x, y, radius):
        print("API 2 drawing a circle at ({}, {} with radius {})".format(x, y, radius))


class Circle(object):
    '''Implementation-independent abstraction: for example, there could be a rectangle class'''
    
    def __init__(self, x, y, radius, drawing_api):
        '''Initialize the necessary attributes'''
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api
    def draw(self):
        '''Implementation-specific abstraction taken care of by another class: DrawigAPI'''
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        '''Implemntation-indepenment'''
        self._radius = percent

#Build the first circle object using API ONE
circle1 = Circle(1, 2, 3, DrawingAPIOne())
#Draw A CIRCLE
circle1.draw()
#Build the second Circle object usin API TWO
circle2 = Circle(2, 3, 4, DrawingAPIOne())
#Draw a circle
circle2.draw()