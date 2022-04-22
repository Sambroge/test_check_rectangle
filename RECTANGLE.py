class Rectangle:
    def __init__(self, a, b=5):
        self.side_a = a
        self.side_b = b

    def get_side_a(self):
        return self.side_a

    def get_side_b(self):
        return self.side_b

    def area(self):
        return 2 * (self.side_a + self.side_b)

    def perimeter(self):
        return self.side_a * self.side_b

    def is_square(self):
        return self.side_a == self.side_b

    def replace_sides(self):
        self.side_a, self.side_b = self.side_b, self.side_a


class ArrayRectangles:
    __rectangle_array = []

    def __init__(self, length, arrays=None):
        self.__rectangle_array = []
        self.length = length
        if arrays:
            if all([isinstance(i, Rectangle) for i in arrays]):
                self.arrays = arrays

    def add_rectangle(self, rectangle):
        if self.length != len(self.__rectangle_array):
            self.__rectangle_array.append(rectangle)
            return True
        return False

    def number_max_area(self):
        variables_area = [i.area() for i in self.__rectangle_array] if self.__rectangle_array else None
        return variables_area.index(max(variables_area)) if variables_area else False

    def number_min_perimeter(self):
        variables_of_perimeter = [i.perimeter() for i in self.__rectangle_array] if self.__rectangle_array else None
        return variables_of_perimeter.index(min(variables_of_perimeter)) if variables_of_perimeter else False

    def number_square(self):
        return sum([i.is_square() for i in self.__rectangle_array])


#foo = Rectangle(10)
#doo = Rectangle(5)
#coo = Rectangle(6, 9)
#print(foo.area())
#print(doo.area())
#print(coo.area())
#print(foo.get_side_a())
#print(doo.perimeter())
#print(coo.get_side_b())
#print(doo.is_square())
#print(coo.is_square())
#print(coo.get_side_b())
#print(coo.get_side_a())
#coo.replace_sides()
#print(coo.get_side_b())
#print(coo.get_side_a())
#print('\n\n\n')
#arr = ArrayRectangles(3)
#arr.add_rectangle(coo)
#arr.add_rectangle(foo)
#arr.add_rectangle(doo)
#print(arr.number_square())
#print(arr.number_max_area())
#print(arr.number_min_perimeter())