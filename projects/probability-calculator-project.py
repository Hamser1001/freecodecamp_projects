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
    probability_successed = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        success = True
        for color, count in expected_balls.items():
            if drawn.count(color) < count:
                success = False
                break
        if success:
            probability_successed += 1
    return round(probability_successed / num_experiments, 2)


hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={"red": 2, "green": 1},
    num_balls_drawn=5,
    num_experiments=2000,
)
print(probability)
