import copy
import random


class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        for color in kwargs.keys():
            self.contents.extend([color] * kwargs[color])

    def draw(self, balls_to_draw: int) -> list:
        if balls_to_draw >= len(self.contents):
            drawn_balls = copy.copy(self.contents)
            self.contents = []
            return drawn_balls
        drawn_balls = []
        for _ in range(balls_to_draw):
            balls_index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(balls_index))
        return drawn_balls


def experiment(
    hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int
) -> float:
    succes_count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_dict = {}
        for ball in drawn_balls:
            drawn_dict[ball] = drawn_dict.get(ball, 0) + 1
        succes = True
        for color, count in expected_balls.items():
            if drawn_dict.get(color, 0) < count:
                succes = False
                break
        if succes:
            succes_count += 1

    return succes_count / num_experiments
