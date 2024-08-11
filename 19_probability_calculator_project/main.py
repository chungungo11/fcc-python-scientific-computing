import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        # Add all colors to the contents list
        for color, amount in balls.items():
            for i in range(amount):
                self.contents.append(color)
        # print('All balls:', self.contents, '\n')

    def draw(self, num_balls):
        removed_balls = []
        if num_balls > len(self.contents):
            return self.contents
        for i in range(num_balls):
            random_ball = random.randint(0,len(self.contents)-1)
            removed_balls.append(self.contents[random_ball])
            self.contents.remove(self.contents[random_ball])
        # print('All removed balls:', removed_balls, '\n')
        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_count = 0
    for i in range(num_experiments):
        expected_balls_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        for color in drawn_balls:
            if color in expected_balls_copy:
                expected_balls_copy[color] -= 1

        if all(x <= 0 for x in expected_balls_copy.values()):
            successful_count += 1
    
    return successful_count / num_experiments


# hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

# print(hat1.draw(5))

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=10)

# print(hat)