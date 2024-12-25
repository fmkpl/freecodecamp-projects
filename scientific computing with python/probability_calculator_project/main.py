import copy
import random

class Hat:
    def __init__(self, **kwargs):
        if len(kwargs.items()) == 0:
            kwargs['red'] = 1

        self.contents = [color for color, amount in kwargs.items() for _ in range(amount) if amount > 0]

    def draw(self, num_balls_drawn):
        if num_balls_drawn == 0:
            return []

        balls_to_draw = []
        if num_balls_drawn > len(self.contents):
            balls_to_draw = self.contents
            self.contents = []
            return balls_to_draw

        balls_to_draw = [self.contents.pop(random.randint(0, len(self.contents) - 1)) for _ in range(num_balls_drawn)]
        return balls_to_draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        if all([balls_drawn.count(color) >= amount for color, amount in expected_balls.items()]):
            M += 1

    return M / num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)