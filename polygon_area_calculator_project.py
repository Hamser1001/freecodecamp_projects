class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

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
        picture = ""
        for _ in range(self.height):
            picture += f"{'*' * self.width}\n"
        return picture

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    pass


rect = Rectangle(10, 5)
print(rect)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())


# 50
# 26
# Rectangle(width=10, height=3)
# **********
# **********
# **********
