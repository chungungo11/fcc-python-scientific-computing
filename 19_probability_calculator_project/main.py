import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []
        # Add all colors to the contents list
        for color, amount in balls.items():
            for i in range(amount):
                self.contents.append(color)

    def draw(self, num_balls):
        # Return all balls if amount of drawn balls exceeds balls in hat
        if num_balls > len(self.contents):
            contents_copy = self.contents.copy()
            self.contents = []
            return contents_copy
        
        drawn_balls = []
        # Draw a random ball, remove it from hat and add it to a new list
        for _ in range(num_balls):
            ball = self.contents.pop(random.randrange(len(self.contents)))
            drawn_balls.append(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_count = 0
    # Start and repeat experiment
    for _ in range(num_experiments):
        # Create copies to prevent continuous randomization
        expected_balls_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Decrease value if expected ball is indeed drawn
        for color in drawn_balls:
            if color in expected_balls_copy:
                expected_balls_copy[color] -= 1

        #  Experiment is successful if values are smaller or equal to zero
        if all(x <= 0 for x in expected_balls_copy.values()):
            successful_count += 1
    
    # Return the probability
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