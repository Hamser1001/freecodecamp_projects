import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num):
        drawn_balls = []
        if num > len(self.contents):
            all_balls = self.contents.copy()
            self.contents = []
            return all_balls
        else:
            for _ in range(num):
                ball = random.choice(self.contents)
                self.contents.remove(ball)
                drawn_balls.append(ball)
            return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


hat = Hat(yellow=4, red=2)
hat2 = Hat(red=5, orange=4, black=1, blue=0, pink=2, yellow=9)

print(hat.contents)
print(hat2.contents)


# print(hat)
print(f"the results: {hat2.draw(200)}")

probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000,
)
