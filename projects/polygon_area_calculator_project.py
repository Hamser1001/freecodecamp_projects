class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        # width * height
        return self.width * self.height

    def get_perimeter(self):
        # 2 * width + 2 * height
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        # (width ** 2 + height ** 2) ** .5
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""

        for _ in range(self.height):
            picture += f"{'*' * self.width}\n"
        return picture

    def get_amount_inside(self, other_shape):
        return (self.width // other_shape.width) * (self.height // other_shape.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, new_side):
        self.side = new_side
        self.width = new_side
        self.height = new_side

    def set_width(self, new_side):
        self.side = new_side
        self.width = new_side
    
    def set_height(self, new_side):
        self.side = new_side
        self.height = new_side

    def __str__(self):
        return f"Square(side={self.side})"


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