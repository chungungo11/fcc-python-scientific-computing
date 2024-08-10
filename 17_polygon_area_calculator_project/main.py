class Rectangle:
    def __init__(self, width, height):
        self.width = self.set_width(width)
        self.height = self.set_height(height)

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
        self.height = height
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return f'Too big for picture.'
        else:
            str_width = ''
            for num in range(0, self.width):
                str_width += '*'

            str_rectangle = ''
            for num in range(0, self.height):
                if num == self.height - 1:
                    str_rectangle += str_width
                else:
                    str_rectangle += str_width + '\n'
            return str_rectangle

    def get_amount_inside(self, shape):
        pass

class Square(Rectangle):
    def __init__(self, length):
        self.set_width(length)
        self.set_height(length)        
        super().__init__(width=self.width, height=self.height)
        self.set_side(length)

    def __str__(self):
        return f'Square(side={self.side})'
    
    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
        return self.side, self.width, self.height

    def set_width(self, length):
        self.width = length
        self.side = length
        return self.width, self.side

    def set_height(self, length):
        self.height = length
        self.side = length
        return self.height, self.side


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(4)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))