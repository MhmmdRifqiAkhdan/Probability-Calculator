import copy
import random


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, number):
    drawn_balls = []
    for i in range(min(number, len(self.contents))):
      drawn_ball = random.choice(self.contents)
      self.contents.remove(drawn_ball)
      drawn_balls.append(drawn_ball)
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  successful_experiments = 0
  for i in range(num_experiments):
    temp_hat = copy.deepcopy(hat)
    drawn_balls = temp_hat.draw(num_balls_drawn)
    ball_counts = {}
    for ball in drawn_balls:
      if ball in ball_counts:
        ball_counts[ball] += 1
      else:
        ball_counts[ball] = 1
    successful = True
    for ball, count in expected_balls.items():
      if ball not in ball_counts or ball_counts[ball] < count:
        successful = False
        break
    if successful:
      successful_experiments += 1
  return successful_experiments / num_experiments
