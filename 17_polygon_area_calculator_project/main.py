class Rectangle:
    # Assign width and height by calling corresponding methods
    def __init__(self, width, height):
        self.width = self.set_width(width)
        self.height = self.set_height(height)

    # String representation of Rectangle instance
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    # Assign and return width
    def set_width(self, width):
        self.width = width
        return self.width

    # Assign and return height
    def set_height(self, height):
        self.height = height
        return self.height

    # Calculate and return area size
    def get_area(self):
        return self.width * self.height

    # Calculate and return perimeter length
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # Calculate and return diagonal length
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # Return string that represents the shape
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return f'Too big for picture.'
        else:
            str_width = ''
            for num in range(0, self.width):
                str_width += '*'

            str_rectangle = ''
            for num in range(0, self.height):
                str_rectangle += str_width + '\n'
            return str_rectangle

    # Calculate and return the number of times the passed in shape could fit inside the shape (with no rotations)
    def get_amount_inside(self, shape):
        horizontal_count = 0
        # Count the number of times the passed in width fits
        while self.width >= shape.width:
            self.width -= shape.width
            horizontal_count += 1
        
        vertical_count = 0
        # Count the number of times the passed in height fits
        while self.height >= shape.height:
            self.height -= shape.height
            vertical_count += 1

        # Calculate and return the number of times
        if horizontal_count == 0 or vertical_count == 0:
            return 0
        else:
            return horizontal_count * vertical_count

            
class Square(Rectangle):
    def __init__(self, length):
        # Set width and height by calling corresponding methods 
        self.set_width(length)
        self.set_height(length)
        # Call parent class and assign width and height 
        super().__init__(width=self.width, height=self.height)
        # Set side by calling corresponding method
        self.set_side(length)

    # String representation of Square instance
    def __str__(self):
        return f'Square(side={self.side})'
    
    # Assign and return side, width and height
    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
        return self.side, self.width, self.height

    # Assign and return width
    def set_width(self, length):
        self.width = length
        self.side = length
        return self.width, self.side

    # Assign and return height
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

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

print(Rectangle(15,10).get_amount_inside(Square(5)))
print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))
print(Rectangle(2,3).get_amount_inside(Rectangle(3, 6)))