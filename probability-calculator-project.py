import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self):
        pass


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


hat = Hat(yellow=4, red=2)
hat2 = Hat(red=5, orange=4, black=1, blue=0, pink=2, yellow=9)

print(hat.contents)
print(hat2.contents)
